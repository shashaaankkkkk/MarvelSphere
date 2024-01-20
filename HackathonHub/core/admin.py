from django.contrib import admin
from .models import Subject , ClassSchedule , Faculty
# Register your models here.
admin.site.register([Subject,ClassSchedule,Faculty])