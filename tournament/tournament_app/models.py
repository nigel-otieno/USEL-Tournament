from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

class Tournament(models.Model):
    ROUND_CHOICES = [
        (1, '1 Round'),
        (2, '2 Rounds'),
        (3, '3 Rounds'),
    ]
    TIMEZONE_CHOICES = [
        ('America/Los_Angeles', 'PST'),
        ('America/New_York', 'EST'),
        ('America/Chicago', 'CST'),
        ('America/Denver', 'MST'),
        ('UTC', 'UTC')
    ]

    GAME_MODE_CHOICES = [
        ('TimeAttack', 'Time Attack: Complete the objective in the shortest time possible.'),
        ('HighestScore', 'Highest Score: Achieve the highest score to win.'),
    ]
    
    TOURNAMENT_TYPE_CHOICES = [
        ('RoboSports', 'RoboSports: Teams design 2 robots that compete with robots of another team.'),
        ('RoboMission', 'RoboMission: Build and program a robot that solves challenges on a field.'),
        ('FutureEngineers', 'FutureEngineers: Highest Score: Achieve the highest score to win.'),
        ('FutureInnovators', 'FutureInnovators: Develop a robot project that helps solve real world problems.'),
    ]

    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500, null=True)
    rules = models.CharField(max_length=500, null=True)
    date = models.DateTimeField()
    time = models.TimeField()
    image = models.ImageField(upload_to='tournament_images/', null=True, blank=True)
    location = models.CharField(max_length=255)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_tournaments')
    rounds = models.IntegerField(choices=ROUND_CHOICES, default=1, help_text="Number of rounds")
    game_mode = models.CharField(max_length=200, choices=GAME_MODE_CHOICES, default='TimeAttack')
    tournament_type = models.CharField(max_length=200, choices=TOURNAMENT_TYPE_CHOICES, default='RoboSports')
    video_url = models.URLField(max_length=500, blank=True, null=True)
    timezone = models.CharField(max_length=500, choices=TIMEZONE_CHOICES, default='UTC')
    closed = models.BooleanField(default=False)

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
    score_one_edited = models.BooleanField(default=False)  # Add this field
    score_two = models.IntegerField(null=True, blank=True)
    score_two_edited = models.BooleanField(default=False)  # Add this field
    score_three = models.IntegerField(null=True, blank=True)
    score_three_edited = models.BooleanField(default=False)  # Add this field
    total_score = models.IntegerField(null=True, blank=True)
    time_score_one = models.DurationField(null=True, blank=True)
    time_score_one_edited = models.BooleanField(default=False)  # Add this field
    time_score_two = models.DurationField(null=True, blank=True)
    time_score_two_edited = models.BooleanField(default=False)  # Add this field
    time_score_three = models.DurationField(null=True, blank=True)
    time_score_three_edited = models.BooleanField(default=False)  # Add this field
    time_total_score = models.DurationField(null=True, blank=True)
    video_url = models.URLField(max_length=250, blank=True, null=True)
    coach_email = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.name


class Bracket(models.Model):
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE, related_name='brackets')
    team = models.ManyToManyField(Team, related_name='brackets')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    state = models.JSONField(default=dict)
    def __str__(self):
        return f"Bracket for {self.tournament.name}"