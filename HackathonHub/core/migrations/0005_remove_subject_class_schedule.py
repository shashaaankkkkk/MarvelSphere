# Generated by Django 3.2.13 on 2024-01-20 17:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_alter_subject_instructors'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subject',
            name='class_schedule',
        ),
    ]
