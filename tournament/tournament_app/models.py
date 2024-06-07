from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

class TimeBasedGameMode(models.Model):
    ROUND_CHOICES = [
        (1, '1 Round'),
        (2, '2 Rounds'),
        (3, '3 Rounds'),
    ]

    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='time_based_created')
    created_at = models.DateTimeField(auto_now_add=True)
    rounds = models.IntegerField(choices=ROUND_CHOICES, default=1, help_text="Number of rounds")
    time_score = models.DurationField(help_text="Time limit (minutes and seconds)", null=True, blank=True)

    def __str__(self):
        return self.name

class ScoreBasedGameMode(models.Model):
    ROUND_CHOICES = [
        (1, '1 Round'),
        (2, '2 Rounds'),
        (3, '3 Rounds'),
    ]

    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='score_based_created')
    created_at = models.DateTimeField(auto_now_add=True)
    rounds = models.IntegerField(choices=ROUND_CHOICES, default=1, help_text="Number of rounds")

    def __str__(self):
        return self.name

class HybridGameMode(models.Model):
    ROUND_CHOICES = [
        (1, '1 Round'),
        (2, '2 Rounds'),
        (3, '3 Rounds'),
    ]

    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='hybrid_created')
    created_at = models.DateTimeField(auto_now_add=True)
    rounds = models.IntegerField(choices=ROUND_CHOICES, default=1, help_text="Number of rounds")
    time_score = models.DurationField(help_text="Time limit (minutes and seconds)", null=True, blank=True)

    def __str__(self):
        return self.name

class Tournament(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateField()
    time = models.TimeField()
    image = models.ImageField(upload_to='tournament_images/', null=True, blank=True)
    location = models.CharField(max_length=255)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_tournaments')

    game_mode_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, null=True, blank=True)
    game_mode_id = models.PositiveIntegerField(null=True, blank=True)
    game_mode = GenericForeignKey('game_mode_type', 'game_mode_id')

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
