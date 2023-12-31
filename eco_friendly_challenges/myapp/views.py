from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from .models import Challenge, CompletedChallenge
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views import generic
import random
import logging
import json


def home(request):
    #challenges = Challenge.objects.all()  # Fetch all challenges
    #return render(request, 'home.html', {'challenges': challenges})

    challenges = list(Challenge.objects.all())
    completed_challenge_ids = set(CompletedChallenge.objects.filter(user=request.user).values_list('challenge_id', flat=True))
    if challenges:
        featured_challenge = random.choice(challenges)
        challenges.remove(featured_challenge)
    else:
        featured_challenge = None
    return render(request, 'home.html', {
        'featured_challenge': featured_challenge,
        'challenges': challenges,
        'completed_challenge_ids': completed_challenge_ids,
    })


class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')  # Redirect to login page after successful registration
    template_name = 'registration/signup.html'  # Path to your signup template


@login_required
def mark_challenge_completed(request):
    try:
        if request.method == 'POST':
            #challenge_id = request.POST.get('challenge_id')
            data = json.loads(request.body)
            challenge_id = int(data.get('challenge_id'))  # Convert to integer
            logging.info(f"Received challenge ID: {challenge_id}")  # Log the received ID
            challenge = Challenge.objects.get(id=challenge_id)
            CompletedChallenge.objects.create(user=request.user, challenge=challenge)
            return JsonResponse({'status': 'success'})
        return JsonResponse({'status': 'error'}, status=400)
    except Exception as e:
        logging.error(f"Error in mark_challenge_completed: {e}")
        return JsonResponse({'status': 'error', 'message': str(e)}, status=500)