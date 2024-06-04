from django import forms
from .models import Tournament, Team, Players, Bracket

class TournamentForm(forms.ModelForm):
    class Meta:
        model = Tournament
        fields = ['name', 'date', 'time', 'image', 'location']

class TeamForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = ['name', 'video_url', 'guardian_name', 'guardian_contact', 'score_one', 'score_two', 'score_three']

class PlayerForm(forms.ModelForm):
    class Meta:
        model = Players
        fields = [
            'first_name', 'last_name', 'age', 'emergency_contact_first_name',
            'emergency_contact_last_name', 'emergency_contact_phone_number',
            'country', 'state_province', 'zip_code', 'address'
        ]
