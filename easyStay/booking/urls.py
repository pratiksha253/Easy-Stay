from django.urls import path
from . import views

urlpatterns = [
    path('create/<int:building_id>', views.CreateBooking.as_view(), name='book'),
    path('bookings/', views.Bookings.as_view(), name='bookings')
    
    
]