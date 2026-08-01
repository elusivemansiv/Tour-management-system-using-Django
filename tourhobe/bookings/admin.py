from django.contrib import admin
from unfold.admin import ModelAdmin
from .models import Booking, HotelBooking, FlightBooking

@admin.register(Booking)
class BookingAdmin(ModelAdmin):
    list_display = ('user', 'package', 'status', 'travel_date')
    list_filter = ('status',)
    search_fields = ('user__username', 'package__title')

@admin.register(HotelBooking)
class HotelBookingAdmin(ModelAdmin):
    list_display = ('user', 'hotel', 'status', 'check_in', 'check_out')
    list_filter = ('status',)
    search_fields = ('user__username', 'hotel__name')

@admin.register(FlightBooking)
class FlightBookingAdmin(ModelAdmin):
    list_display = ('user', 'flight', 'status', 'travel_date')
    list_filter = ('status', 'fare_class')
    search_fields = ('user__username', 'flight__airline')