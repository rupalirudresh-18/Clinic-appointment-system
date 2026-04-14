from accounts.utils import is_doctor, is_patient
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from doctors.models import TimeSlot
from .models import Appointment, VisitNote
from .forms import AppointmentForm, VisitNoteForm

@login_required
def book_appointment(request, slot_id):
    if not is_patient(request.user):
        messages.error(request, 'Only patients can book appointments.')
        return redirect('home')

    slot = get_object_or_404(TimeSlot, id=slot_id, is_available=True)

    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            appointment = form.save(commit=False)
            appointment.patient = request.user
            appointment.doctor = slot.doctor
            appointment.slot = slot
            appointment.save()

            slot.is_available = False
            slot.save()

            messages.success(request, 'Appointment booked successfully.')
            return redirect('my_appointments')
    else:
        form = AppointmentForm()

    return render(request, 'appointments/book_appointment.html', {'form': form, 'slot': slot})

@login_required
def my_appointments(request):
    appointments = Appointment.objects.filter(patient=request.user).order_by('-created_at')
    return render(request, 'appointments/my_appointments.html', {'appointments': appointments})


@login_required
def cancel_appointment(request, appointment_id):
    appointment = get_object_or_404(Appointment, id=appointment_id, patient=request.user)

    appointment.status = 'cancelled'
    appointment.slot.is_available = True
    appointment.slot.save()
    appointment.save()

    messages.success(request, 'Appointment cancelled.')
    return redirect('my_appointments')


@login_required
def update_queue_status(request, appointment_id, status):
    appointment = get_object_or_404(Appointment, id=appointment_id, doctor=request.user)
    appointment.status = status
    appointment.save()
    messages.success(request, 'Queue status updated.')
    return redirect('doctor_appointments')


@login_required
def doctor_appointments(request):
    if not is_doctor(request.user):
        messages.error(request, 'Only doctors can view doctor appointments.')
        return redirect('home')

    appointments = Appointment.objects.filter(doctor=request.user).order_by('-created_at')
    return render(request, 'appointments/doctor_appointments.html', {'appointments': appointments})


@login_required
def add_visit_note(request, appointment_id):
    if not is_doctor(request.user):
        messages.error(request, 'Only doctors can add visit notes.')
        return redirect('home')

    appointment = get_object_or_404(Appointment, id=appointment_id, doctor=request.user)
    note, created = VisitNote.objects.get_or_create(appointment=appointment)

    if request.method == 'POST':
        form = VisitNoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            messages.success(request, 'Visit note saved successfully.')
            return redirect('doctor_appointments')
    else:
        form = VisitNoteForm(instance=note)

    return render(request, 'appointments/add_visit_note.html', {'form': form, 'appointment': appointment})

@login_required
def view_visit_note(request, appointment_id):
    if not is_patient(request.user):
        messages.error(request, 'Only patients can view visit notes.')
        return redirect('home')

    appointment = get_object_or_404(Appointment, id=appointment_id, patient=request.user)
    note = VisitNote.objects.filter(appointment=appointment).first()

    return render(request, 'appointments/view_visit_note.html', {
        'appointment': appointment,
        'note': note
    })