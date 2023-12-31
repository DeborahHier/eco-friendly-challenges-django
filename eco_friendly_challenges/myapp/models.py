from django.db import models
from django.contrib.auth.models import User

class Challenge(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    # Add more fields as needed

    def __str__(self):
        return self.title

class UserChallenge(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    challenge = models.ForeignKey(Challenge, on_delete=models.CASCADE)
    date_completed = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.challenge.title}"

class CompletedChallenge(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    challenge = models.ForeignKey(Challenge, on_delete=models.CASCADE)
    completed_on = models.DateTimeField(auto_now_add=True)