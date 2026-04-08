from django.urls import path
from . import views

urlpatterns = [
    path('', views.flight_list, name='flight_list'),
    path('<int:pk>/book/', views.flight_booking_init, name='flight_booking'),
]
