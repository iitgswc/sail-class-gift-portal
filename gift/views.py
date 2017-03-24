from django.contrib import auth
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ValidationError
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.utils.http import is_safe_url
from django.views.generic import View
from .models import Option, Student, Transaction
from .forms import LoginForm, TransactionForm
from django.db.models import F
from datetime import datetime


class LoginView(View):
    """7
    View class for handling login functionality.
    """
    template_name = 'gift/login.html'
    port = 995
    next = ''

    def get(self, request):
        self.next = request.GET.get('next', '')
        if request.user.is_authenticated() and not request.user.is_superuser:
            return redirect('gift:option')
        args = dict(form=LoginForm(None), next=self.next)
        return render(request, self.template_name, args)

    def post(self, request):
        redirect_to = request.POST.get('next', self.next)
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            server = form.cleaned_data.get('login_server')

            print("calling authenticate function in django")
            user = auth.authenticate(username=username, password=password,
                                     server=server, port=self.port)
            print(user)
            # if user is not None and user.is_active:
            if user is not None:
                if not is_safe_url(url=redirect_to, host=request.get_host()):
                    auth.login(request=request, user=user)

                    return redirect('gift:option')
                else:
                    return redirect(redirect_to)
            # elif not user.is_active:
            #     form.add_error(None, 'User login has been disabled')
            #     return render(request, self.template_name, dict(form=form))
            else:
                form.add_error(None, 'No user exists for given credentials.')
                return render(request, self.template_name, dict(form=form))
        else:
            return render(request, self.template_name, dict(form=form))


class OptionView(LoginRequiredMixin, View):
    login_url = reverse_lazy('gift:login')
    template_name = 'gift/options.html'

    def get(self, request):
        return render(request, self.template_name)


class DonateView(LoginRequiredMixin, View):
    login_url = reverse_lazy('gift:login')
    template_name = 'gift/transactionid.html'

    def get(self, request):
        args = dict(form=TransactionForm(None))
        return render(request, self.template_name, args)

    def post(self, request):
        print(request)
        form = TransactionForm(request.POST)
        if form.is_valid():
            transactionid = form.cleaned_data.get('transactionid')
            t = Transaction()
            t.id_of_donater = request.user.id
            t.webmail_of_donater = request.user.username
            t.transactionid = transactionid
            t.created_at = datetime.now()
            t.save()
            template_name = 'gift/thankyou.html'
            return render(request, template_name)

        else:
            return render(request, self.template_name, dict(form=form))


class ChoiceView(LoginRequiredMixin, View):
    login_url = reverse_lazy('gift:login')
    template_name = 'gift/choice.html'

    choices = Option.objects.exclude(price=0)
    endorement_fund = Option.objects.get(price=0)
    context = {'choices': choices,
               'endorement_fund': endorement_fund}

    def get(self, request):
        u = Student.objects.get(user=request.user)
        if int(u.choice) == -1:
            return render(request, self.template_name, self.context)
        else:
            return render(request, 'gift/alreadyfilled.html')

    def post(self, request):
        choice = request.POST.get("choice", "")
        if int(choice) != 100:
            # selected=self.choices[int(choice)-1].name
            option = Option.objects.get(pk=choice)
            option.count = F('count') + 1
            option.save()
        else:
            option = Option.objects.get(price=0)
            option.count = F('count') + 1
            option.save()

        u = Student.objects.get(user=request.user)
        u.choice = choice
        u.choice_filled_at = datetime.now()
        u.save()

        template_name = 'gift/thankyou.html'
        return render(request, template_name)


class LogoutView(LoginRequiredMixin, View):
    """
    View class for handling logout.
    """
    login_url = reverse_lazy('gift:login')
    raise_exception = False
    http_method_names = ['get', 'head', 'options']

    def get(self, request):
        auth.logout(request=request)
        return redirect('gift:login')
