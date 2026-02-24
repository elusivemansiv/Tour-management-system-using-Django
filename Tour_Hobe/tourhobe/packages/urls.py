from django.urls import path
from .views import home, location_packages
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('explore/', views.explore, name='explore'),
    path('packages/', views.all_packages, name='all_packages'),
    path('location/<int:location_id>/', views.location_packages, name='location_packages'),
    path('package/<int:pk>/', views.package_detail, name='package_detail'),
    path("contact/", views.contact, name="contact"),
    path("about/", views.about, name="about"),
]