from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import TimeSlotForm
from .models import TimeSlot
from accounts.utils import is_doctor

@login_required
def manage_slots(request):
    if not is_doctor(request.user):
        messages.error(request, 'Only doctors can manage slots.')
        return redirect('home')

    if request.method == 'POST':
        form = TimeSlotForm(request.POST)
        if form.is_valid():
            slot = form.save(commit=False)
            slot.doctor = request.user
            slot.save()
            messages.success(request, 'Time slot added successfully.')
            return redirect('manage_slots')
    else:
        form = TimeSlotForm()

    slots = TimeSlot.objects.filter(doctor=request.user).order_by('-date', 'start_time')
    return render(request, 'doctors/manage_slots.html', {'form': form, 'slots': slots})