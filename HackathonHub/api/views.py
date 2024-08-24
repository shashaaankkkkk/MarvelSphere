from django.shortcuts import render
from django.http import HttpResponse , JsonResponse
from rest_framework.decorators import api_view
from core import models
# Create your views here.
@api_view(['get','view'])
def hello(request):
    return JsonResponse({"messgae":"hello"})

def subject(request):
    projects = models.project.objects.all().values(
        'id', 'project_id', 'name', 'description', 'department', 'semester_year',
        'instructors__name', 'student__name', 'textbooks_materials', 'assessment_methods_syllabus'
    )
    return JsonResponse(list(projects),safe=False)
