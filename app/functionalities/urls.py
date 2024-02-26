from django.urls import path
from functionalities import views

from django.urls import path
from functionalities import views

urlpatterns = [
    # path('list/', views.FunctionalitiesListView.as_view(), name='funct_list'),
    # path('<int:pk>/', views.FunctionalitiesDetailView.as_view(), name='funct_detail'),
    path("signup/", views.SignupView.as_view(), name="signup")
]