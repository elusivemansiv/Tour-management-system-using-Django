from django.contrib import admin
from unfold.admin import ModelAdmin, TabularInline
from django.utils.html import mark_safe
from .models import FlightOffer, PopularDestination, Flight, FlightSegment, FlightFare

@admin.register(FlightOffer)
class FlightOfferAdmin(ModelAdmin):
    list_display = ('title', 'discount_percentage', 'image_preview')
    readonly_fields = ('image_preview',)

    def image_preview(self, obj):
        if obj.image and hasattr(obj.image, 'url'):
            return mark_safe(f'<img src="{obj.image.url}" style="max-height: 100px; border-radius: 8px;" />')
        return "No image"
    image_preview.short_description = 'Preview'

@admin.register(PopularDestination)
class PopularDestinationAdmin(ModelAdmin):
    list_display = ('city', 'country', 'image_preview')
    readonly_fields = ('image_preview',)

    def image_preview(self, obj):
        if obj.image and hasattr(obj.image, 'url'):
            return mark_safe(f'<img src="{obj.image.url}" style="max-height: 100px; border-radius: 8px;" />')
        return "No image"
    image_preview.short_description = 'Preview'

class FlightSegmentInline(TabularInline):
    model = FlightSegment
    extra = 1

class FlightFareInline(TabularInline):
    model = FlightFare
    extra = 1

@admin.register(Flight)
class FlightAdmin(ModelAdmin):
    list_display = ('airline', 'logo_preview', 'origin', 'destination', 'departure_time', 'base_price')
    list_filter = ('airline', 'origin', 'destination')
    readonly_fields = ('logo_preview',)
    inlines = [FlightSegmentInline, FlightFareInline]

    def logo_preview(self, obj):
        if obj.logo and hasattr(obj.logo, 'url'):
            return mark_safe(f'<img src="{obj.logo.url}" style="max-height: 50px; border-radius: 8px;" />')
        return "No logo"
    logo_preview.short_description = 'Logo'
