from django.shortcuts import render
from .models import Room, Message

def index(request):

    mensage = Message.objects.filter(user=request.user.id)

    context = {'msg': mensage}

    return render(request, 'pages/index.html', context)
