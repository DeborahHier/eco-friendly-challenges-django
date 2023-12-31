from django.shortcuts import render
from django.http import HttpResponse
from .models import Challenge
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic

def home(request):
    #return HttpResponse("Hello, world! This is my first Django page.")
    challenges = Challenge.objects.all()  # Fetch all challenges
    return render(request, 'home.html', {'challenges': challenges})

class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')  # Redirect to login page after successful registration
    template_name = 'registration/signup.html'  # Path to your signup template
