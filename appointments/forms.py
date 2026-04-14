from django import forms
from .models import Appointment, VisitNote

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['reason']


class VisitNoteForm(forms.ModelForm):
    class Meta:
        model = VisitNote
        fields = ['symptoms', 'prescription', 'doctor_notes']