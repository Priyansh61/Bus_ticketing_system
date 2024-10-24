from django.db import models
from accounts.models import Account

BOOKING_STATUS = [
    ('Pending', 'Pending'),
    ('Confirmed', 'Confirmed'),
    ('Cancelled', 'Cancelled'),
]

class Route(models.Model) :
    route_name = models.CharField(max_length=100)
    route_from = models.CharField(max_length=100)
    route_to = models.CharField(max_length=100)
    route_price = models.IntegerField()
    route_time = models.TimeField()
    
    def __str__(self):
        return f"{self.route_name} - {self.route_from} to {self.route_to}"

    
class Bus(models.Model) :
    bus_name = models.CharField(max_length=100)
    bus_number = models.CharField(max_length=100)
    bus_capacity = models.IntegerField()
    bus_route = models.ForeignKey(Route, on_delete=models.CASCADE)
    days_of_operation = models.CharField(max_length=100)
    
    def __str__(self):
        return f"{self.bus_name} - {self.bus_number}"

class Seat(models.Model) :
    seat_number = models.IntegerField()
    seat_status = models.BooleanField(default=False)
    bus = models.ForeignKey(Bus, on_delete=models.CASCADE)

    class Meta:
        indexes = [
            models.Index(fields=['seat_number', 'bus']),
        ]
        unique_together = ('seat_number', 'bus')

    def __str__(self):
        return f"{self.seat_number} - {self.seat_status}"   
# Create your models here.


class Order(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    order_email = models.EmailField(max_length=100)
    order_phone_number = models.CharField(max_length=15)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=50, choices=BOOKING_STATUS)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order {self.id} by {self.user.email}"


class Booking(models.Model) :
    bus = models.ForeignKey(Bus, on_delete=models.CASCADE)
    seat = models.ForeignKey(Seat, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    user_name = models.CharField(max_length=100)
    booking_price = models.IntegerField()
    
    def __str__(self):
        return f"Booking for Seat {self.seat.seat_number} on Bus {self.bus.bus_name}"


