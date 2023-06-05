from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.contrib.auth.views import LoginView
from django.views.generic import (
    ListView,
    CreateView,
    DetailView,
    DeleteView,
    FormView
)
from .models import UserApp
from django.contrib.auth import get_user_model
from . import forms
from django.urls import reverse_lazy
from django.shortcuts import redirect


class Index(View):
    def get(self, request):
        return render(request, 'base.html')


class Register(FormView):
    template_name = 'register.html'
    form_class = forms.RegisterForm
    success_url = 'login'

    def form_valid(self, form):
        print(form.cleaned_data)
        user = form.save()
        print(user)
        print("to jest sztos")
        return super().form_valid(form)

    def form_invalid(self, form):
        print(form.errors)
        return super().form_invalid(form)

class Login(LoginView):
    template_name = 'login.html'
    redirect_authenticated_user = 'index'


class RoomCreate(CreateView):
    pass


class Room(DetailView):
    pass
