# booking/views.py

from rest_framework import viewsets
from .models import Route, Bus, Seat, Booking
from .serializers import RouteSerializer, BusSerializer, SeatSerializer, BookingSerializer
from rest_framework.decorators import api_view
from django.db import transaction
from .models import Bus, Seat, Booking, Order


# {
#   "bus_id": 1,
#   "seats": [
#     {"seat_number": 5, "user_name": "Alice"},
#     {"seat_number": 6, "user_name": "Bob"}
#   ],
#   "email": "testuser@example.com",
#   "phone_number": "1234567890"
# }
@api_view(['POST'])
def create_booking(request):
    user = request.user
    bus_id = request.data.get('bus_id')
    seats_to_book = request.data.get('seats') 
    order_email = request.data.get('email')
    order_phone_number = request.data.get('phone_number')

    if not seats_to_book:
        return Response({'error': 'No seats to book'}, status=status.HTTP_400_BAD_REQUEST)

    try:
        bus = Bus.objects.get(id=bus_id)
    except Bus.DoesNotExist:
        return Response({'error': 'Bus not found'}, status=status.HTTP_404_NOT_FOUND)

    try:
        with transaction.atomic():
            total_price = 0
            bookings = []

            order = Order.objects.create(
                user=user,
                order_email=order_email,
                order_phone_number=order_phone_number,
                total_price=total_price,  
                status='Pending'
            )

            # Loop through each seat to create individual bookings
            for seat_info in seats_to_book:
                seat_number = seat_info.get('seat_number')
                user_name = seat_info.get('user_name')

                if not seat_number or not user_name:
                    return Response({'error': 'Each seat must have a seat number and user name'}, status=status.HTTP_400_BAD_REQUEST)

                try:
                    seat = Seat.objects.select_for_update().get(bus=bus, seat_number=seat_number)
                except Seat.DoesNotExist:
                    return Response({'error': f'Seat {seat_number} not found'}, status=status.HTTP_404_NOT_FOUND)

                if seat.seat_status:
                    return Response({'error': f'Seat {seat_number} is already booked'}, status=status.HTTP_400_BAD_REQUEST)

                seat.seat_status = True
                seat.save()

                total_price += bus.bus_route.route_price

                booking = Booking(
                    bus=bus,
                    seat=seat,
                    order=order,
                    user_name=user_name,
                    booking_price=bus.bus_route.route_price
                )

                bookings.append(booking)

            order.total_price = total_price
            order.status = 'Confirmed'
            order.save()

            Booking.objects.bulk_create(bookings)

            return Response({'message': 'Booking successful', 'order_id': order.id}, status=status.HTTP_201_CREATED)

    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class RouteViewSet(viewsets.ModelViewSet):
    queryset = Route.objects.all()
    serializer_class = RouteSerializer

class BusViewSet(viewsets.ModelViewSet):
    queryset = Bus.objects.all()
    serializer_class = BusSerializer

class SeatViewSet(viewsets.ModelViewSet):
    queryset = Seat.objects.all()
    serializer_class = SeatSerializer

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
