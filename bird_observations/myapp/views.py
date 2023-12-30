from django.shortcuts import render
from django.http import HttpResponse
from .models import Challenge

def home(request):
    #return HttpResponse("Hello, world! This is my first Django page.")
    challenges = Challenge.objects.all()  # Fetch all challenges
    return render(request, 'home.html', {'challenges': challenges})
