from django.contrib import admin
from unfold.admin import ModelAdmin, TabularInline
from .models import Hotel, Room, Review

class RoomInline(TabularInline):
    model = Room
    extra = 1

@admin.register(Hotel)
class HotelAdmin(ModelAdmin):
    list_display = ('name', 'location', 'tier', 'star_rating', 'price_per_night')
    search_fields = ('name', 'location')
    list_filter = ('tier', 'star_rating')
    inlines = [RoomInline]

@admin.register(Review)
class ReviewAdmin(ModelAdmin):
    list_display = ('hotel', 'user_name', 'rating', 'created_at')
    list_filter = ('rating', 'created_at')
    search_fields = ('user_name', 'hotel__name')
