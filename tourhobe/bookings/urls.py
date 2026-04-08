from django.urls import path
from . import views

urlpatterns = [
    path('book/<int:package_id>/', views.book_package, name='book_package'),
    path('my-bookings/', views.my_bookings, name='my_bookings'),
]