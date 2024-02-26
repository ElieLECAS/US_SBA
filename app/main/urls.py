from django.urls import path
from main import views

from . import views

urlpatterns = [
    path('', views.home_page, name='home'),
    path('api_page/', views.api_page, name='api_page'),
]