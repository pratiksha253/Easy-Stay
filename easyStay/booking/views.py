from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Booking
from mainapp.models import Building
from django.views.generic import CreateView, ListView
from django.urls import reverse_lazy

from .forms import BookingForm

class CreateBooking(CreateView):
    model = Booking
    template_name = 'booking.html'
    form_class = BookingForm
    success_url = reverse_lazy('bookings')
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)



class Bookings(ListView):
    model = Booking
    template_name = 'bookings.html'
    context_object_name = 'bookings'

