from django.shortcuts import render, redirect
from .models import Booking


def home(request):
    context = {}
    return render(request, 'home.html', context)


def booking(request):
    if request.method == 'POST':
        Booking.objects.create(
            name=request.POST.get('name'),
            phone=request.POST.get('phone'),
            service=request.POST.get('service'),
            booking_date=request.POST.get('booking_date'),
            booking_time=request.POST.get('booking_time')
        )
        return render(request, 'booking.html', {'success': True})

    return render(request, 'booking.html')
