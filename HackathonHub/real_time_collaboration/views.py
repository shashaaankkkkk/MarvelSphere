from django.shortcuts import render

 # Import the Room database model
from .models import Room

# View for the rooms
def rooms(request):
    rooms = Room.objects.all()

    return render(request, 'room/rooms.html', {'rooms': rooms})
def room(request, pk):
    room = Room.objects.get(pk=pk)

    return render(request, 'room/room.html', {'room': room})
# hackathon/views.py

from django.shortcuts import render

def code_editor_view(request):
    return render(request, 'chat_rooms.html')
