from django.shortcuts import render
from doctors.models import TimeSlot

def welcome(request):
    return render(request, 'welcome.html')

def home(request):
    is_doctor = request.user.is_authenticated and request.user.groups.filter(name='Doctor').exists()
    is_patient = request.user.is_authenticated and request.user.groups.filter(name='Patient').exists()

    if is_doctor:
        available_slots = TimeSlot.objects.filter(
            doctor=request.user,
            is_available=True
        ).order_by('date', 'start_time')
    else:
        available_slots = TimeSlot.objects.filter(
            is_available=True
        ).order_by('date', 'start_time')

    return render(request, 'dashboard/home.html', {
        'available_slots': available_slots,
        'is_doctor': is_doctor,
        'is_patient': is_patient,
    })


def admin_dashboard(request):
    return render(request, 'dashboard/admin_dashboard.html')