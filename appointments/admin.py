from django.contrib import admin
from .models import Appointment, VisitNote

admin.site.register(Appointment)
admin.site.register(VisitNote)