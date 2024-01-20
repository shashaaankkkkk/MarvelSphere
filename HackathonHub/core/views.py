from .models import ClassSchedule

from django.shortcuts import render , redirect
from django.http import HttpResponse ,JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# Create your views here.

@login_required
def index(request):
    return  render(request,"core/index.html")


from .models import Subject, ClassSchedule, Faculty

def subjects_and_schedules(request):
    # Fetch all subjects
    subjects = Subject.objects.all()

    # Fetch all class schedules
    class_schedules = ClassSchedule.objects.all()

    # Fetch all faculty members
    faculties = Faculty.objects.all()

    # You can add more context data if needed

    context = {
        'subjects': subjects,
        'class_schedules': class_schedules,
        'faculties': faculties,
    }
    print(context)
    return render(request, 'core/index.html', context)

# views.py



