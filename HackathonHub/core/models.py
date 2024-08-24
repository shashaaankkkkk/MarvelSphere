from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync


class project(models.Model):
    project_id = models.CharField(max_length=10)
    name = models.CharField(max_length=100)
    description = models.TextField()
    department = models.CharField(max_length=50)
    semester_year = models.CharField(max_length=20)
    instructors = models.ForeignKey('Faculty', on_delete=models.CASCADE)
    student=models.ForeignKey("Student",on_delete=models.CASCADE)
    textbooks_materials = models.TextField()
    assessment_methods_syllabus = models.TextField()

    def __str__(self):
        return self.name 

class ProjectSchedule(models.Model):
 
    date = models.DateField(default='2024-01-01')  # Set a default value here
    start_time = models.TimeField(default='08:00')
    end_time = models.TimeField(default='09:30')
    channel_name = models.CharField(max_length=255, blank=True, null=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if not self.channel_name:
            # Create a unique channel name for the class
            self.channel_name = f"class_{self.id}"
            self.save()


    def __str__(self):
        return f"{self.subject.name} - {self.date} - {self.start_time} to {self.end_time}"

def create_class_channel(sender, instance, **kwargs):
    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_add)(f"class_{instance.id}", "dummy_channel")

class Faculty(models.Model):
    name = models.CharField(max_length=100)
    department = models.CharField(max_length=50)
    position = models.CharField(max_length=50)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)

    def __str__(self):
        return self.name

class Student(models.Model):
    name = models.CharField(max_length=100)
    department = models.CharField(max_length=50)
    course = models.CharField(max_length=50)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)

    def __str__(self):
        return self.name
