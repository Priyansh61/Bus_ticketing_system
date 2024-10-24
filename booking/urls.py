# booking/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RouteViewSet, BusViewSet, SeatViewSet, BookingViewSet
from .views import create_booking

router = DefaultRouter()
router.register(r'routes', RouteViewSet)
router.register(r'buses', BusViewSet)
router.register(r'seats', SeatViewSet)
router.register(r'bookings', BookingViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('create_booking/', create_booking, name='create_booking')
]
