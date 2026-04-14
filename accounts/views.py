from django.shortcuts import render, redirect
from django.contrib.auth.models import Group
from django.contrib.auth import login
from django.contrib import messages
from .forms import PatientRegisterForm
from .models import PatientProfile

def register_patient(request):
    if request.method == 'POST':
        form = PatientRegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            patient_group, created = Group.objects.get_or_create(name='Patient')
            user.groups.add(patient_group)

            PatientProfile.objects.create(
                user=user,
                phone=''
            )

            login(request, user)
            messages.success(request, 'Patient account created successfully.')
            return redirect('home')
    else:
        form = PatientRegisterForm()

    return render(request, 'accounts/register.html', {'form': form})