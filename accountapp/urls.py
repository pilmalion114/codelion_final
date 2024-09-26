from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from accountapp.views import main, AccountCreateView

app_name = 'accountapp'

urlpatterns = [
    path('main/', main, name='main'),
    path('create/', AccountCreateView.as_view(), name='create'),
    path('login/', LoginView.as_view(template_name='accountapp/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]