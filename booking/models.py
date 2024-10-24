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
    bus_id = models.ForeignKey(Bus, on_delete=models.CASCADE)

    class Meta:
        indexes = [
            models.Index(fields=['seat_number', 'bus_id']),
        ]
        unique_together = ('seat_number', 'bus_id')

    def __str__(self):
        return f"{self.seat_number} - {self.seat_status}"   
# Create your models here.

class Booking(models.Model) :
    bus_id = models.ForeignKey(Bus, on_delete=models.CASCADE)
    seat_id = models.ForeignKey(Seat, on_delete=models.CASCADE)
    user_id = models.ForeignKey(Account, on_delete=models.CASCADE)
    booking_date = models.DateField(auto_now_add=True)
    booking_time = models.TimeField(auto_now_add=True)
    booking_status = models.CharField(max_length=100, choices=BOOKING_STATUS)
    booking_price = models.IntegerField()
    booking_email = models.EmailField(max_length=100)
    booking_phone = models.CharField(max_length=15)
    
    def __str__(self):
        return f"{self.bus_id} - {self.seat_id} - {self.booking_date} - {self.booking_time} - {self.booking_status}"