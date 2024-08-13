from django.test import TestCase
from .models import User, Tournament, Team
from django.utils import timezone
from .forms import *
class Tournament_Model_Test(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='nigel', password='12345')
    
    def test_index_page_returns_response(self):
        response = self.client.get('/')
        
        self.assertTemplateUsed(response, 'index.html')
        self.assertEqual(response.status_code, 200)
        
    def test_index_page_has_name(self):
        # Correct field name and include all required fields
        tourney = Tournament.objects.create(
            name='USEL',
            date=timezone.now(),
            time=timezone.now().time(),
            location='Sample Location',
            created_by=self.user
        )
        self.assertEqual(tourney.name, 'USEL')
        
class Tournament_Model_Tournament_and_Page_Response(TestCase):
    
    def setUp(self):
        self.user = User.objects.create(username="nigel", password="123456")
        self.tournament = Tournament.objects.create(name='usel', date=timezone.now(), time=timezone.now().time(), location='upland', created_by=self.user)
        
    def test_detail_tournament_page_response(self):
        response = self.client.get('/tournaments/')
        
        self.assertTemplateUsed(response, 'tournaments.html')
        self.assertEqual(response.status_code, 200)
        
class Tournament_Model_Detail_Test(TestCase):
    def setUp(self):
        self.user = User.objects.create(username="nigel", password="123456")
        self.tournament = Tournament.objects.create(name='usel', date=timezone.now(), time=timezone.now().time(), location='upland', created_by=self.user)
        self.tournament2 = Tournament.objects.create(name='usel2', date=timezone.now(), time=timezone.now().time(), location='upland', created_by=self.user)

    def test_detail_tournament_page_response(self):
        response = self.client.get(f'/tournament/{self.tournament.id}/')
        
        self.assertTemplateUsed(response, 'tournament_detail.html')
        self.assertEqual(response.status_code, 200)
        
    def test_detail_page_has_corrrct_content(self):
        response = self.client.get(f'/tournament/{self.tournament.id}/')
        
        self.assertContains(response, self.tournament.name)
        self.assertContains(response, self.tournament.description)
        self.assertNotContains(response, self.tournament2.name)
        
class New_Page_Test_Tournament(TestCase):
    
    def setUp(self):
        
        self.form = TeamForm
        self.user = User.objects.create_user(username="nigel", password="123456")
        self.client.login(username='nigel', password='123456')  # Log in the user
        self.tournament = Tournament.objects.create(name='usel', date=timezone.now(), time=timezone.now().time(), location='upland', created_by=self.user)

    def test_get_request_is_correct(self):
        response = self.client.get(f'/tournament/{self.tournament.id}/create_team/')
        self.assertTemplateUsed(response, 'team_create.html')
        self.assertEqual(response.status_code, 200)
        
    def test_form_is_valid(self):
        self.assertTrue(issubclass(self.form, TeamForm))
        self.assertTrue('name' in self.form.Meta.fields)
        
        form = self.form({
            'name': 'Team Red'
        })
        
        self.assertTrue(form.is_valid())
    
    def test_page_has_form(self):
        response = self.client.get(f'/tournament/{self.tournament.id}/create_team/')
        self.assertContains(response, '<form')
        self.assertContains(response, '<label')
        self.assertContains(response, 'csrfmiddlewaretoken')
        
class New_Page_Tes_Is_Valid(TestCase):
    
    def setUp(self):
        self.form = TournamentForm
        self.user = User.objects.create_user(username="nigel", password="123456")
        self.client.login(username='nigel', password='123456')  # Log in the user
        self.tournament = Tournament.objects.create(name='usel', date=timezone.now(), time=timezone.now().time(), location='upland', created_by=self.user)

    def test_update_form_returrns_correct_response(self):
        response = self.client.get(f'/tournament/{self.tournament.id}/edit/')
        self.assertTemplateUsed('tournament_edit')
        self.assertTemplateNotUsed('tournament')
        self.assertEqual(response.status_code, 200)
        
    