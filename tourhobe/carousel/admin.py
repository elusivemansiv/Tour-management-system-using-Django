from django.contrib import admin
from .models import CarouselSlide

from unfold.admin import ModelAdmin

@admin.register(CarouselSlide)
class CarouselSlideAdmin(ModelAdmin):
    pass
