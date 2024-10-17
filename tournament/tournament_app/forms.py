from django import forms
from .models import *

class TournamentForm(forms.ModelForm):
    class Meta:
        model = Tournament
        fields = [
            'name', 'description', 'rules', 'date', 'time', 'location',
            'rounds', 'game_mode', 'tournament_type', 'image', 'video_url'
        ]
        widgets = {
            'rounds': forms.RadioSelect,
            'game_mode': forms.RadioSelect,
            'tournament_type': forms.RadioSelect, 
        }
class TeamForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = ['name', 'coach_email']

class PlayerForm(forms.ModelForm):
    class Meta:
        model = Players
        fields = [
            'first_name', 'last_name', 'age' 
            , 'state_province', 'country'
        ]

class BracketForm(forms.ModelForm):
    class Meta:
        model = Bracket
        fields = ['tournament', 'team', 'state']