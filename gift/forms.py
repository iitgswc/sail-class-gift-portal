from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext as _

LOGIN_SERVER = [
    ('202.141.80.9', 'naambor'),
    ('202.141.80.10', 'disang'),
    ('202.141.80.11', 'tamdil'),
    ('202.141.80.12', 'teesta'),
    ('202.141.80.13', 'dikrong'),
]

class LoginForm(forms.Form):
    username = forms.CharField(required=True, label='Webmail')
    password = forms.CharField(required=True, widget=forms.PasswordInput)
    login_server = forms.ChoiceField(required=True, choices=LOGIN_SERVER)

    def clean_login_server(self):
        valid_servers = ['202.141.80.9', '202.141.80.10', '202.141.80.11',
                         '202.141.80.12', '202.141.80.13']
        login_server = self.cleaned_data.get('login_server')
        if login_server not in valid_servers:
            raise ValidationError(_('Invalid Login Server'), code='invalid')
        return login_server

class TransactionForm(forms.Form):
    transactionid = forms.IntegerField(required=True, label='Transaction Id',min_value=1000,max_value=100000000)
