from django.contrib import admin
from .models import Challenge, UserChallenge, CompletedChallenge

@admin.register(Challenge)
class ChallengeAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description')  # Add 'id' here

admin.site.register(UserChallenge)
admin.site.register(CompletedChallenge)

