from django import forms
from .models import *
from pytz import all_timezones

class TournamentForm(forms.ModelForm):

    class Meta:
        model = Tournament
        fields = [
            'name', 'description', 'rules', 'date', 'time', 'location',
            'rounds', 'game_mode', 'tournament_type', 'image', 'video_url', 'timezone'
        ]
        widgets = {
            'date': forms.DateInput(format='%m/%d/%Y', attrs={'type': 'text', 'placeholder': 'MM/DD/YYYY', 'class': 'form-control'}),
            'rounds': forms.RadioSelect,
            'game_mode': forms.RadioSelect,
            'tournament_type': forms.RadioSelect, 
            'timezone': forms.Select(attrs={'class': 'form-control'}),

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