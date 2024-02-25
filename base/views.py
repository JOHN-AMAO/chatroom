from django.shortcuts import render
from django.http import HttpResponse
from .models import Room
# Create your views here.


def home(request):
    return HttpResponse("This is the homepage")

def room(request):
    rooms = Room.objects.all()
    context = {"rooms": rooms}
    return render(request, "room.html", context)

def school(request):

    return render( request,"school.html")