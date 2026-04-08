from django.urls import path
from . import views

urlpatterns = [
    path('hotel/<int:pk>/', views.hotel_detail, name='hotel_detail'),
    path('hotels/', views.hotel_list, name='hotel_list'),
]
