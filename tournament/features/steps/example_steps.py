from behave import given, when, then
from django.urls import reverse
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from tournament_app.models import Tournament, User
from django.test import Client

@given('I am a logged-in user')
def step_impl(context):
    user = User.objects.create_user(username='user', email='user@example.com', password='password')
    context.browser = webdriver.Chrome()  # or use another WebDriver, like Firefox
    context.browser.get(context.get_url('/accounts/login/'))
    context.browser.find_element_by_name('username').send_keys('user')
    context.browser.find_element_by_name('password').send_keys('password')
    context.browser.find_element_by_name('submit').click()

@given('I have joined or created a tournament')
def step_impl(context):
    context.tournament = Tournament.objects.create(name="Championship", user=context.user)
    context.client = Client()
    context.client.force_login(context.user)

@when('I go to the tournament detail page')
def step_impl(context):
    context.response = context.client.get(reverse('tournament_detail', args=[context.tournament.id]))

@when('I click the create team button')
def step_impl(context):
    context.response = context.client.get(reverse('create_team', args=[context.tournament.id]))  # Assumes a view named 'create_team'

@when('I fill out the team create form')
def step_impl(context):
    form_data = {'name': 'New Team', 'tournament': context.tournament.id}
    context.response = context.client.post(reverse('create_team', args=[context.tournament.id]), form_data)

@when('I submit the team create form')
def step_impl(context):
    # This step might be redundant as the form submit might be covered in 'I fill out the team create form'
    pass

@then('I should be redirected back to my tournament')
def step_impl(context):
    assert context.response.status_code == 302  # Checks for redirect
    assert context.response['Location'] == reverse('tournament_detail', args=[context.tournament.id])

@then('I will see my new team listed on the tournament')
def step_impl(context):
    context.response = context.client.get(reverse('tournament_detail', args=[context.tournament.id]))
    assert 'New Team' in context.response.content.decode()