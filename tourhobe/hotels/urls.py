from django.urls import path
from . import views

urlpatterns = [
    path('hotel/<int:pk>/', views.hotel_detail, name='hotel_detail'),
    path('hotel/<int:pk>/checkout/', views.hotel_checkout, name='hotel_checkout'),
    path('hotels/', views.hotel_list, name='hotel_list'),
]
