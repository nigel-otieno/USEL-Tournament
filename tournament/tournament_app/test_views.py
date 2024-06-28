from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Tournament, Team

class TournamentViewTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.tournament = Tournament.objects.create(
            name="Test Tournament",
            description="Test Description",
            rules="Test Rules",
            date="2024-07-01T00:00:00Z",
            time="12:00:00",
            location="Test Location",
            created_by=self.user,
            tournament_type='RoboSports'
        )

    def test_tournament_list_view(self):
        response = self.client.get(reverse('tournaments'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Tournament")

    def test_tournament_detail_view(self):
        response = self.client.get(reverse('tournament_detail', args=[self.tournament.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Tournament")
        self.assertContains(response, "RoboSports")  # Check for tournament type

    def test_tournament_create_view(self):
        self.client.login(username='testuser', password='12345')
        response = self.client.post(reverse('tournament_create'), {
            'name': 'New Tournament',
            'description': 'Description',
            'rules': 'Rules',
            'date': '2024-08-01T00:00:00Z',
            'time': '14:00:00',
            'location': 'Location',
            'rounds': 1,
            'game_mode': 'TimeAttack',
            'tournament_type': 'RoboSports'  # Add this line
        })
        self.assertEqual(response.status_code, 302)  # Redirects after creation

class TeamViewTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.tournament = Tournament.objects.create(
            name="Test Tournament",
            description="Test Description",
            rules="Test Rules",
            date="2024-07-01T00:00:00Z",
            time="12:00:00",
            location="Test Location",
            created_by=self.user,
            tournament_type='RoboSports'
        )
        self.team = Team.objects.create(
            name="Test Team",
            created_by=self.user
        )
        self.team.tournament.add(self.tournament)

    def test_team_detail_view(self):
        response = self.client.get(reverse('team_detail', args=[self.team.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Team")
