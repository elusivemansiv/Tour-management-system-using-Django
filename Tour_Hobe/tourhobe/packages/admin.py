from django.contrib import admin
from .models import Location, Package, CarouselSlide, Country

@admin.register(Package)
class PackageAdmin(admin.ModelAdmin):
    filter_horizontal = ('hotels',)
    list_display = ('title', 'location', 'price', 'duration')

admin.site.register(Country)
admin.site.register(Location)
admin.site.register(CarouselSlide)