from django.conf.urls import url
from . import views
app_name='gift'

urlpatterns = [
    url(r'^$', views.LoginView.as_view(), name='login'),
    url(r'^login/$', views.LoginView.as_view(), name='login'),
    url(r'^option/$',views.OptionView.as_view(), name='option'),
    url(r'^donate/$',views.DonateView.as_view(), name='donate'),
    url(r'^choice/$',views.ChoiceView.as_view(), name='choice'),
    url(r'^logout/$', views.LogoutView.as_view(), name='logout'),
    url(r'^.*/$', views.LoginView.as_view(), name='login'),

]