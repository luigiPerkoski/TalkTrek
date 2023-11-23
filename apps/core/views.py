from django.shortcuts import render
from .models import Room, Message

def index(request):

    messages = Message.objects.filter(user=request.user.id)
    rooms = Room.objects.filter(user=request.user.id)


    context = {
        'messages': messages,
        'rooms': rooms,
    }

    return render(request, 'pages/index.html', context)

def mensagens(request):
    ...
