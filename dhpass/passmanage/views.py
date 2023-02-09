from django.shortcuts import render
from django.views import generic


class Home(generic.TemplateView):
    template_name = 'passmanage/home.html'


class Login(generic.TemplateView):
    template_name = 'passmanage/login.html'

    def sign_in(self):
        """Signin Function"""
        return


class Register(generic.TemplateView):
    template_name = 'passmanage/register.html'


class Passwords:
    pass


class AddPassword:
    pass


class PasswordDetails:
    pass
