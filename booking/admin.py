from django.contrib import admin
from .models import Bus, Route, Booking

class BusAdmin(admin.ModelAdmin):
    list_display = ['bus_name', 'bus_number', 'bus_capacity', 'bus_route', 'days_of_operation']
    search_fields = ['bus_name', 'bus_number', 'bus_capacity', 'bus_route', 'days_of_operation']
    list_filter = ['bus_name', 'bus_number', 'bus_capacity', 'bus_route', 'days_of_operation']
    list_per_page = 10


class RouteAdmin(admin.ModelAdmin):
    list_display = ['route_name', 'route_from', 'route_to', 'route_price', 'route_time']
    search_fields = ['route_name', 'route_from', 'route_to', 'route_price', 'route_time']
    list_filter = ['route_name', 'route_from', 'route_to', 'route_price', 'route_time']
    list_per_page = 10

class SeatAdmin(admin.ModelAdmin):
    list_display = ['seat_number', 'seat_status', 'bus_id']
    search_fields = ['seat_number', 'seat_status', 'bus_id']
    list_filter = ['seat_number', 'seat_status', 'bus_id']
    list_per_page = 10

class BookingAdmin(admin.ModelAdmin):
    list_display = ['bus_id', 'seat_id','booking_price', 'order_id', 'user_name']
    search_fields = ['bus_id', 'seat_id','booking_price', 'order_id', 'user_name']
    list_filter = ['bus_id', 'seat_id','booking_price', 'order_id', 'user_name']
    list_per_page = 10

admin.site.register(Bus, BusAdmin)
admin.site.register(Route, RouteAdmin)
admin.site.register(Booking, BookingAdmin)

# Register your models here.
