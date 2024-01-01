from django.test import TestCase
from django.contrib.auth.models import User
from .models import Challenge, UserChallenge, CompletedChallenge
from django.utils import timezone
import datetime

class ChallengeModelTest(TestCase):
    def setUp(self):
        Challenge.objects.create(title='Challenge 1', description='Description 1')
    
    def test_challenge_creation(self):
        challenge = Challenge.objects.get(id=1)
        self.assertEqual(challenge.title, 'Challenge 1')
        self.assertEqual(challenge.description, 'Description 1')

class UserChallengeModelTest(TestCase):
    def setUp(self):
        user = User.objects.create_user('testuser', 'test@example.com', 'testpass')
        challenge = Challenge.objects.create(title='Challenge 1', description='Description 1')
        UserChallenge.objects.create(user=user, challenge=challenge)
    
    def test_user_challenge_creation(self):
        user_challenge = UserChallenge.objects.get(id=1)
        self.assertEqual(user_challenge.user.username, 'testuser')
        self.assertEqual(user_challenge.challenge.title, 'Challenge 1')
