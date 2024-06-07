# tournament_app/urls.py
from django.urls import path
from .views import *
from . import views

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('tournaments/', TournamentsView.as_view(), name='tournaments'),
    path('tournament/<int:pk>/', TournamentDetailView.as_view(), name='tournament_detail'),
    path('tournament/<int:id>/edit/', tournament_edit, name='tournament_edit'),
    path('tournament/<int:tournament_id>/create_team/', team_create, name='team_create'),
    path('team/<int:team_id>/create_player/', player_create, name='player_create'),
    path('team/<int:pk>/', TeamDetailView.as_view(), name='team_detail'),
    path('team/<int:team_id>/upload_video/', views.upload_video, name='upload_video'),
    path('player/<int:pk>/', PlayerDetailView.as_view(), name='player_detail'),
    path('tournament/<int:tournament_id>/bracket/create/', views.bracket_create, name='bracket_create'),
    path('tournament/<int:tournament_id>/bracket/display/', views.bracket_display, name='bracket_display'),
    path('tournament/create/', game_mode_selection, name='game_mode_selection'),
    path('tournament/create/<str:game_mode>/', views.tournament_create, name='tournament_create'),
    path('tournament/<int:tournament_id>/game_mode/edit/', views.game_mode_edit, name='game_mode_edit'),
    path('tournament/<int:tournament_id>/delete/', tournament_delete, name='tournament_delete'),

]
