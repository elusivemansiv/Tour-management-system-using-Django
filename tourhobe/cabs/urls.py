from django.urls import path
from . import views

urlpatterns = [
    path('', views.cab_home, name='cab_home'),
    path('list/', views.cab_list, name='cab_list'),
    path('<int:pk>/', views.cab_detail, name='cab_detail'),
    path('<int:pk>/book/', views.cab_checkout, name='cab_checkout'),
]
