def is_doctor(user):
    return user.is_authenticated and user.groups.filter(name='Doctor').exists()

def is_patient(user):
    return user.is_authenticated and user.groups.filter(name='Patient').exists()

def is_admin(user):
    return user.is_authenticated and user.is_superuser