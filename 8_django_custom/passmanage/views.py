from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.views import generic
from django.urls import reverse, reverse_lazy

from .models import User
from .forms import *


class Home(generic.TemplateView):
    template_name = 'passmanage/home.html'


class Login(LoginView):
    model = User
    form_class = AuthenticationForm
    redirect_authenticated_user = True
    redirect_field_name = reverse_lazy('home')
    template_name = 'passmanage/login.html'
    success_url = reverse_lazy('home')

    # TEMP CHANGE^ REROUTE TO DASHBOARD

    # def get_context_data(self):
    #     """Used with"""
    #     context = super().get_context_data()
    #     context['form'] = self.form_class(self.request.POST or None)
    #     return context

    def form_valid(self, form):
        if self.request.user.is_authenticated:
            messages.success(self.request, "You are already logged in as %s " % self.request.user)
            return super().form_valid(form)
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(self.request, username=username, password=password)
        if user is not None:
            login(self.request, user)
            return super().form_valid(form)
        else:
            messages.warning(self.request, 'Please enter the correct password!')
            # return render(self.request, self.template_name, {'form': form})
            return super().form_invalid(form)


class Register(generic.TemplateView):
    template_name = 'passmanage/register.html'


# @login_required()
class Dashboard(generic.TemplateView):
    template_name = 'passmanage/dashboard.html'


class AddPassword:
    pass


class PasswordDetails:
    pass
