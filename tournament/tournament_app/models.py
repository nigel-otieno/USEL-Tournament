# tournament_app/models.py
from django.contrib.auth.models import User
from django.db import models

class Players(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.IntegerField()
    emergency_contact_first_name = models.CharField(max_length=100)
    emergency_contact_last_name = models.CharField(max_length=100)
    emergency_contact_phone_number = models.CharField(max_length=15)
    country = models.CharField(max_length=100)
    state_province = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=10)
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Tournament(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateField()
    time = models.TimeField()
    location = models.CharField(max_length=255)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_tournaments')

    def __str__(self):
        return self.name

class Team(models.Model):
    name = models.CharField(max_length=100)
    tournament = models.ManyToManyField(Tournament, related_name='teams')
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_teams')
    members = models.ManyToManyField(Players, related_name='teams')
    video_url = models.URLField(max_length=250, blank=True, null=True)
    guardian_name = models.CharField(max_length=255, blank=True, null=True) 
    guardian_contact = models.CharField(max_length=15, blank=True, null=True)  
    
    def __str__(self):
        return self.name
