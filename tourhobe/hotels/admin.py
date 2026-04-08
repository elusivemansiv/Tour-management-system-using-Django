from django.contrib import admin
from .models import Hotel, Room

class RoomInline(admin.TabularInline):
    model = Room
    extra = 1

@admin.register(Hotel)
class HotelAdmin(admin.ModelAdmin):
    list_display = ('name', 'location', 'tier', 'star_rating', 'price_per_night')
    search_fields = ('name', 'location')
    list_filter = ('tier', 'star_rating')
    inlines = [RoomInline]
