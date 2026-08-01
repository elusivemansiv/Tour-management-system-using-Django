from django.urls import path
from .views import home, location_packages
from . import views
from about.views import about
from blog.views import blog_page, blog_detail

urlpatterns = [
    path('', views.home, name='home'),
    path('explore/', views.explore, name='explore'),
    path('packages/', views.all_packages, name='all_packages'),
    path('location/<int:location_id>/', views.location_packages, name='location_packages'),
    path('country/<int:country_id>/', views.country_packages, name='country_packages'),
    path('package/<int:pk>/', views.package_detail, name='package_detail'),
    path("contact/", views.contact, name="contact"),
    path("about/", about, name="about"),
    path("blog/", blog_page, name="blog_page"),
    path("blog/<int:post_id>/", blog_detail, name="blog_detail"),
]