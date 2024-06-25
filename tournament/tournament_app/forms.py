from django import forms
from .models import *

class TournamentForm(forms.ModelForm):
    class Meta:
        model = Tournament
        fields = ['name', 'date', 'time', 'rules', 'location', 'game_mode', 'rounds', 'image']
        widgets = {
            'rounds': forms.RadioSelect,
            'game_mode': forms.RadioSelect,
        }

# class GameModeSelectionForm(forms.Form):
#     GAME_MODE_CHOICES = [
#         ('TimeBasedGameMode', 'Time Based Game Mode'),
#         ('ScoreBasedGameMode', 'Score Based Game Mode'),
#         ('HybridGameMode', 'Hybrid Game Mode'),
#     ]
#     game_mode = forms.ChoiceField(choices=GAME_MODE_CHOICES, widget=forms.RadioSelect)

# class TimeBasedGameModeForm(forms.ModelForm):
#     class Meta:
#         model = TimeBasedGameMode
#         fields = ['name', 'description',  'rounds', 'time_score']

# class ScoreBasedGameModeForm(forms.ModelForm):
#     class Meta:
#         model = ScoreBasedGameMode
#         fields = ['name', 'description',  'rounds']

# class HybridGameModeForm(forms.ModelForm):
#     class Meta:
#         model = HybridGameMode
#         fields = ['name', 'description',  'rounds', 'time_score']


class TeamForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = ['name', 'video_url', 'coach', 'score_one', 'score_two', 'score_three']

class PlayerForm(forms.ModelForm):
    class Meta:
        model = Players
        fields = [
            'first_name', 'last_name', 'age', 'emergency_contact_first_name',
            'emergency_contact_last_name', 'emergency_contact_phone_number',
            'country', 'state_province', 'zip_code', 'address'
        ]

class BracketForm(forms.ModelForm):
    class Meta:
        model = Bracket
        fields = ['tournament', 'team', 'state']