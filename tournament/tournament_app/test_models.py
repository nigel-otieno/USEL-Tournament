from django.test import TestCase
from django.contrib.auth.models import User
from .models import Tournament, Team, Players

class TournamentModelTest(TestCase):

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

    def test_tournament_creation(self):
        self.assertIsInstance(self.tournament, Tournament)
        self.assertEqual(self.tournament.name, "Test Tournament")
        self.assertEqual(self.tournament.tournament_type, "RoboSports")

class TeamModelTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.team = Team.objects.create(
            name="Test Team",
            created_by=self.user
        )

    def test_team_creation(self):
        self.assertIsInstance(self.team, Team)
        self.assertEqual(self.team.name, "Test Team")

class PlayerModelTest(TestCase):

    def setUp(self):
        self.player = Players.objects.create(
            first_name="John",
            last_name="Doe",
            age=20,
            emergency_contact_first_name="Jane",
            emergency_contact_last_name="Doe",
            emergency_contact_phone_number="1234567890",
            address="123 Street",
            country="Country",
            state_province="State",
            zip_code="12345"
        )

    def test_player_creation(self):
        self.assertIsInstance(self.player, Players)
        self.assertEqual(self.player.first_name, "John")
