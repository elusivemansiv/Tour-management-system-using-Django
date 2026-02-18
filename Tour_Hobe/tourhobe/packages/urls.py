from django.urls import path
from .views import home, location_packages

urlpatterns = [
    path('', home, name='home'),
    
    path('location/<int:location_id>/', location_packages, name='location_packages'),
]