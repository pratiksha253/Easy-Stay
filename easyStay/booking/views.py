from django.shortcuts import render,get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Booking
from mainapp.models import Building

@login_required
def create_booking(request,building_id):
    building = get_object_or_404(Building, id=building_id)
    if request.method == 'POST':
        guests = request.POST.get('guests')
        advance_amount = request.POST.get('advance_amount')
        total_amount = request.POST.get('total_amount')

        booking = Booking.objects.create(
            user=request.user,
            building=building,
            advance_amount=advance_amount,
            total_amount=total_amount,
            booking_date=datetime.now()     
        )
        return redirect('booking_confirm', booking_id=booking.id)

    return render(request, 'create_booking.html', {'building': building})
    
def booking_confirm(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)
    return render(request, 'booking_confirm.html', {'booking': booking})


def booking_success(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)
    return render(request, 'booking_success.html', {'booking': booking})


def booking_cancel(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)
    booking.status = 'cancelled'
    booking.save()
    return redirect('confirm_booking')


