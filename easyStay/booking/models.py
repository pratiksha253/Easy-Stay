from django.db import models
from django.contrib.auth.models import User
from mainapp.models import Building

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    building = models.ForeignKey(Building, on_delete=models.CASCADE)
    advance_amount = models.DecimalField(max_digits=10, decimal_places=2)
    booking_date=models.DateField()
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    status = models.CharField(choices=[
            ('Pending', 'Pending'),
            ('confirmed', 'Confirmed'),
            ('cancelled', 'Cancelled')
        ],default='Pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}'s booking at {self.building.name}"


