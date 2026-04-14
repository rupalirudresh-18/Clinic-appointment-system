from django.urls import path
from . import views

urlpatterns = [
    path('book/<int:slot_id>/', views.book_appointment, name='book_appointment'),
    path('my/', views.my_appointments, name='my_appointments'),
    path('cancel/<int:appointment_id>/', views.cancel_appointment, name='cancel_appointment'),
    path('doctor/', views.doctor_appointments, name='doctor_appointments'),
    path('status/<int:appointment_id>/<str:status>/', views.update_queue_status, name='update_queue_status'),
    path('note/<int:appointment_id>/', views.add_visit_note, name='add_visit_note'),
    path('view-note/<int:appointment_id>/', views.view_visit_note, name='view_visit_note'),
]