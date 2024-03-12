from django.urls import include,path
from main import views

from . import views

urlpatterns = [
    path('', views.home_page, name='home'),
    path('api_page/', views.api_page, name='api_page'),
    path("__reload__/", include("django_browser_reload.urls")),
]