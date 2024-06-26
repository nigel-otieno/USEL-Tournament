from django.urls import path
from .views import *

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('tournaments/', TournamentsView.as_view(), name='tournaments'),
    path('tournament/<int:pk>/', TournamentDetailView.as_view(), name='tournament_detail'),
    path('tournament/create/', tournament_create, name='tournament_create'),
    path('tournament/<int:id>/edit/', tournament_edit, name='tournament_edit'),
    path('tournament/<int:tournament_id>/delete/', tournament_delete, name='tournament_delete'),
    path('tournament/<int:tournament_id>/create_team/', team_create, name='team_create'),
    path('team/<int:team_id>/create_player/', player_create, name='player_create'),
    path('team/<int:pk>/', TeamDetailView.as_view(), name='team_detail'),
    path('team/<int:team_id>/upload_video/', upload_video, name='upload_video'),
    path('player/<int:pk>/', PlayerDetailView.as_view(), name='player_detail'),
    path('update_team_score/', update_team_score, name='update_team_score'),
    path('update_team_time_score/', update_team_time_score, name='update_team_time_score'),
]
