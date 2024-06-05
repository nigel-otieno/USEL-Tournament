from django.db import models
from django.contrib.auth.models import User

class GameMode(models.Model):
    GAME_MODE_CHOICES = [
        ('TA', 'Time Attack'),
        ('VAR', 'Variations in Set Rounds'),
        ('SRHS', 'Single Round Highest Score'),
        ('HTV', 'Hybrid of Time and Variations in Set Rounds'),
        ('HTSRHS', 'Hybrid of Time and Single Round Highest Score'),
    ]
    
    name = models.CharField(max_length=100, choices=GAME_MODE_CHOICES)
    description = models.TextField(blank=True, null=True)
    time_limit = models.DurationField(null=True, blank=True)  # For time-based modes
    max_rounds = models.IntegerField(null=True, blank=True)  # For round-based modes
    score_limit = models.IntegerField(null=True, blank=True)  # For highest score modes

    def __str__(self):
        return self.get_name_display()
    
class Tournament(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateField()
    time = models.TimeField()
    image = models.ImageField(upload_to='tournament_images/', null=True, blank=True)
    location = models.CharField(max_length=255)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_tournaments')
    game_mode = models.ForeignKey(GameMode, on_delete=models.CASCADE, related_name='tournaments', null=True, blank=True)

    def __str__(self):
        return self.name

class Players(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.IntegerField()
    emergency_contact_first_name = models.CharField(max_length=100)
    emergency_contact_last_name = models.CharField(max_length=100)
    emergency_contact_phone_number = models.CharField(max_length=15)
    address = models.CharField(max_length=100, null=True)
    country = models.CharField(max_length=100)
    state_province = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=10)
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Team(models.Model):
    name = models.CharField(max_length=100)
    tournament = models.ManyToManyField(Tournament, related_name='teams')
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_teams')
    members = models.ManyToManyField(Players, related_name='teams')
    score_one = models.IntegerField(null=True, blank=True)
    score_two = models.IntegerField(null=True, blank=True)
    score_three = models.IntegerField(null=True, blank=True)
    video_url = models.URLField(max_length=250, blank=True, null=True)
    guardian_name = models.CharField(max_length=255, blank=True, null=True)
    guardian_contact = models.CharField(max_length=15, blank=True, null=True)
    
    def __str__(self):
        return self.name

class Bracket(models.Model):
    tournament = models.OneToOneField(Tournament, on_delete=models.CASCADE, related_name='bracket')
    state = models.JSONField()

    def __str__(self):
        return f"Bracket for {self.tournament.name}"
