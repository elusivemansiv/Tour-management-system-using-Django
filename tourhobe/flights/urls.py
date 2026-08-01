from django.urls import path
from . import views

urlpatterns = [
    path('', views.flight_home, name='flight_home'),
    path('list/', views.flight_list, name='flight_list'),
    path('<int:pk>/', views.flight_detail, name='flight_detail'),
    path('<int:pk>/checkout/', views.flight_checkout, name='flight_checkout'),
]
