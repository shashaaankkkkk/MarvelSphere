# Generated by Django 3.2.13 on 2024-01-20 21:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_chatmessage_chatroom_codesnippet'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='codesnippet',
            name='room',
        ),
        migrations.RemoveField(
            model_name='codesnippet',
            name='user',
        ),
        migrations.DeleteModel(
            name='ChatMessage',
        ),
        migrations.DeleteModel(
            name='ChatRoom',
        ),
        migrations.DeleteModel(
            name='CodeSnippet',
        ),
    ]
