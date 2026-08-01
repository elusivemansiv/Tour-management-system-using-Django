from django.contrib import admin
from unfold.admin import ModelAdmin, TabularInline
from .models import VehicleType, CabFeature, CabFAQ, Cab, CabImage, CabBooking

@admin.register(VehicleType)
class VehicleTypeAdmin(ModelAdmin):
    pass

@admin.register(CabFeature)
class CabFeatureAdmin(ModelAdmin):
    pass

@admin.register(CabFAQ)
class CabFAQAdmin(ModelAdmin):
    pass

class CabImageInline(TabularInline):
    model = CabImage
    extra = 1

@admin.register(Cab)
class CabAdmin(ModelAdmin):
    list_display = ('title', 'vehicle_type', 'base_price', 'discount_percentage', 'rating')
    inlines = [CabImageInline]

@admin.register(CabBooking)
class CabBookingAdmin(ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'cab', 'trip_type', 'pickup_date', 'status')
    list_filter = ('status', 'trip_type', 'pickup_date')
    search_fields = ('first_name', 'last_name', 'email')
