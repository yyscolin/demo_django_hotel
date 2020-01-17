from django.shortcuts import render
from .models import Room_Type

def rooms(request):
    rooms = Room_Type.objects.all()
    for room in rooms:
        room.images_base = "rooms-" + room.title.lower().replace(' ', '-')
    
    context = {
        "rooms": rooms
    }
    return render(request, 'rooms.html', context)