from django.shortcuts import render
from django.http import HttpResponse , JsonResponse
from rest_framework.decorators import api_view

# Create your views here.
@api_view(['get','view'])
def hello(request):
    return JsonResponse({"messgae":"hello"})