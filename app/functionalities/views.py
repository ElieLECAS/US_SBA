
from django.shortcuts import render
# from .models import Functionalities
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy

# class FunctionalitiesListView(LoginRequiredMixin,ListView):
#     model = Functionalities
#     template_name = "functionalities/funct_list.html"

# class FunctionalitiesDetailView(DetailView):
#     model = Functionalities
#     template_name = "functionalities/funct_detail.html"

class SignupView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = "registration/signup.html"