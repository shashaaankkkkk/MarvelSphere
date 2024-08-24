from django.contrib import admin
from .models import project ,ProjectSchedule, Faculty  , Student
# Register your models here.
admin.site.register([project,ProjectSchedule,Faculty,Student])