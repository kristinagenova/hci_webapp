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
    timeline = [{"date":"17/Nov/2017", "comment":"Monica is still struggling with 'r' sounds."},
        {"date": "5/Nov/2017", "comment": "Some improvements with mouth gymnastics."},
        {"date": "14/Oct/2017", "comment": "Gymnastics were postponed."},
        {"date": "29/Sept/2017", "comment": "Played Kevin says together"},
        {"date": "20/Sept/2017", "comment": "Did gymnastics type 1 and words with 'r' sounds"},
        {"date": "1/Sept/2017", "comment": "Did gymnastics type 4"},
        {"date": "26/Aug/2017", "comment": "Played space game"},
        {"date": "18/Aug/2017", "comment": "First meeting with Monica"}]
    return render(request, 'patient.html', { 'patient': patient, 'timeline': timeline })
