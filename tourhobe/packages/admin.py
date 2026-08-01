from django.contrib import admin
from unfold.admin import ModelAdmin
from .models import Location, Package, Country

@admin.register(Package)
class PackageAdmin(ModelAdmin):
    filter_horizontal = ('hotels',)
    list_display = ('title', 'location', 'price', 'duration')

from django.utils.html import mark_safe

@admin.register(Country)
class CountryAdmin(ModelAdmin):
    list_display = ('name', 'image_preview')
    readonly_fields = ('image_preview',)

    def image_preview(self, obj):
        if obj.image and hasattr(obj.image, 'url'):
            return mark_safe(f'<img src="{obj.image.url}" style="max-height: 100px; border-radius: 8px;" />')
        return "No image"
    image_preview.short_description = 'Preview'

@admin.register(Location)
class LocationAdmin(ModelAdmin):
    list_display = ('name', 'country', 'image_preview')
    readonly_fields = ('image_preview',)
    list_filter = ('country',)

    def image_preview(self, obj):
        if obj.image and hasattr(obj.image, 'url'):
            return mark_safe(f'<img src="{obj.image.url}" style="max-height: 100px; border-radius: 8px;" />')
        return "No image"
    image_preview.short_description = 'Preview'