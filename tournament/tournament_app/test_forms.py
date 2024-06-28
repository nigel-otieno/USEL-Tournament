from django.test import TestCase
from .forms import TournamentForm, TeamForm, PlayerForm

class TournamentFormTest(TestCase):

    def test_valid_form(self):
        form = TournamentForm(data={
            'name': 'Tournament',
            'description': 'Description',
            'rules': 'Rules',
            'date': '2024-07-01T00:00:00Z',
            'time': '12:00:00',
            'location': 'Location',
            'rounds': 1,
            'game_mode': 'TimeAttack',
            'tournament_type': 'RoboSports'
        })
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        form = TournamentForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 9)  # Adjust based on required fields

class TeamFormTest(TestCase):

    def test_valid_form(self):
        form = TeamForm(data={'name': 'Team'})
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        form = TeamForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 1)

class PlayerFormTest(TestCase):

    def test_valid_form(self):
        form = PlayerForm(data={
            'first_name': 'John',
            'last_name': 'Doe',
            'age': 20,
            'emergency_contact_first_name': 'Jane',
            'emergency_contact_last_name': 'Doe',
            'emergency_contact_phone_number': '1234567890',
            'address': '123 Street',
            'country': 'Country',
            'state_province': 'State',
            'zip_code': '12345'
        })
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        form = PlayerForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 10)  # Adjust based on required fields
