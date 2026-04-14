from django.urls import path
from . import views

urlpatterns = [
    path('slots/', views.manage_slots, name='manage_slots'),
]