from django.shortcuts import render
from django.http import HttpResponse , JsonResponse
from rest_framework.decorators import api_view
from core import models
# Create your views here.
@api_view(['get','view'])
def hello(request):
    return JsonResponse({"messgae":"hello"})

def subject(request):
    subject=list(models.Subject.objects.all().values())
    print(subject)
    return JsonResponse(subject,safe=False)