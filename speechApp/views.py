from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .models import Patient

@login_required
def index(request):
    user = request.user
    patients = Patient.objects.filter(doctor__user=user.id)
    return render(request, 'index.html', { 'patients': patients })

@login_required
def patient(request, id):
    patient = Patient.objects.get(pk=id)
    timeline = [0] * 20
    return render(request, 'patient.html', { 'patient': patient, 'timeline': timeline })
