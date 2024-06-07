from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView, TemplateView
from .models import *
from .forms import *
from .bracket import Bracket as BracketClass
import json


@login_required
def game_mode_selection(request):
    if request.method == 'POST':
        form = GameModeSelectionForm(request.POST)
        if form.is_valid():
            game_mode = form.cleaned_data['game_mode']
            return redirect('tournament_create', game_mode=game_mode)
    else:
        form = GameModeSelectionForm()
    return render(request, 'game_mode_selection.html', {'form': form})

@login_required
def tournament_create(request, game_mode):
    game_mode_instance = None
    if game_mode == 'TimeBasedGameMode':
        GameModeForm = TimeBasedGameModeForm
    elif game_mode == 'ScoreBasedGameMode':
        GameModeForm = ScoreBasedGameModeForm
    elif game_mode == 'HybridGameMode':
        GameModeForm = HybridGameModeForm
    else:
        raise ValueError("Invalid game mode")

    if request.method == 'POST':
        form = TournamentForm(request.POST, request.FILES)
        game_mode_form = GameModeForm(request.POST)
        if form.is_valid() and game_mode_form.is_valid():
            tournament = form.save(commit=False)
            tournament.created_by = request.user
            game_mode_instance = game_mode_form.save(commit=False)
            game_mode_instance.created_by = request.user
            game_mode_instance.save()
            tournament.game_mode_type = ContentType.objects.get_for_model(game_mode_instance)
            tournament.game_mode_id = game_mode_instance.id
            tournament.save()
            return redirect('tournament_detail', pk=tournament.pk)
    else:
        form = TournamentForm()
        game_mode_form = GameModeForm()

    return render(request, 'tournament_create.html', {
        'form': form,
        'game_mode_form': game_mode_form,
        'game_mode': game_mode
    })


@login_required
def bracket_create(request, tournament_id):
    tournament = get_object_or_404(Tournament, id=tournament_id)
    teams = [team.name for team in tournament.teams.all()]
    
    try:
        bracket_instance = tournament.bracket
        bracket_data = bracket_instance.state
    except Bracket.DoesNotExist:
        bracket_data = None
    
    if bracket_data:
        bracket = BracketClass(teams, rounds=bracket_data['rounds'], lineup=bracket_data['lineup'])
    else:
        bracket = BracketClass(teams)
    
    if request.method == 'POST':
        if 'shuffle' in request.POST:
            bracket.shuffle()
        elif 'update' in request.POST:
            round_number = int(request.POST['round'])
            team_names = request.POST['teams'].split(',')
            bracket.update(round_number, team_names)
        
        bracket_state = {
            'rounds': bracket.rounds,
            'lineup': bracket.lineup
        }
        if bracket_data:
            bracket_instance.state = bracket_state
            bracket_instance.save()
        else:
            Bracket.objects.create(tournament=tournament, state=bracket_state)
    
    return render(request, 'bracket_create.html', {'bracket': bracket, 'tournament': tournament})


@login_required
def bracket_display(request, tournament_id):
    tournament = get_object_or_404(Tournament, id=tournament_id)
    teams = [team.name for team in tournament.teams.all()]
    
    try:
        bracket_instance = tournament.bracket
        bracket_data = bracket_instance.state
    except Bracket.DoesNotExist:
        bracket_data = None
    
    if bracket_data:
        bracket = BracketClass(teams)
        bracket.rounds = bracket_data['rounds']
        bracket.lineup = bracket_data['lineup']
    else:
        bracket = BracketClass(teams)
    
    return render(request, 'bracket_display.html', {'bracket': bracket, 'tournament': tournament})

@login_required
def tournament_edit(request, id):
    tournament = get_object_or_404(Tournament, id=id)

    if request.user != tournament.created_by:
        return redirect('tournament_detail', pk=tournament.id)

    if request.method == 'POST':
        form = TournamentForm(request.POST, request.FILES, instance=tournament)
        if form.is_valid():
            form.save()
            return redirect('tournament_detail', pk=tournament.id)
    else:
        form = TournamentForm(instance=tournament)

    return render(request, 'tournament_edit.html', {'form': form, 'tournament': tournament})

@login_required
def team_create(request, tournament_id):
    tournament = get_object_or_404(Tournament, id=tournament_id)

    if request.method == 'POST':
        form = TeamForm(request.POST)
        if form.is_valid():
            team = form.save(commit=False)
            team.created_by = request.user
            team.save()
            team.tournament.add(tournament)
            return redirect('tournament_detail', pk=tournament.id)
    else:
        form = TeamForm()

    return render(request, 'team_create.html', {'form': form, 'tournament': tournament})

@login_required
def upload_video(request, team_id):
    team = get_object_or_404(Team, id=team_id)
    if request.user == team.created_by or request.user in team.members.all():
        if request.method == 'POST':
            form = TeamForm(request.POST, instance=team)
            if form.is_valid():
                form.save()
                return redirect('team_detail', pk=team.id)
    return redirect('team_detail', pk=team.id)

@login_required
def player_create(request, team_id):
    team = get_object_or_404(Team, id=team_id)

    if request.user != team.created_by:
        return redirect('team_detail', pk=team.id)

    if team.members.count() >= 3:
        return redirect('team_detail', pk=team.id)

    if request.method == 'POST':
        form = PlayerForm(request.POST)
        if form.is_valid():
            player = form.save(commit=False)
            player.save()
            team.members.add(player)
            return redirect('team_detail', pk=team.id)
    else:
        form = PlayerForm()

    return render(request, 'player_create.html', {'form': form, 'team': team})

@login_required
def player_detail(request, pk):
    player = get_object_or_404(Players, pk=pk)
    team = player.teams.first()
    if request.user != team.created_by:
        return redirect('team_detail', pk=team.id)
    return render(request, 'player_detail.html', {'player': player})

class IndexView(TemplateView):
    template_name = 'index.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tournaments'] = Tournament.objects.all()
        return context
class TournamentsView(ListView):
    model = Tournament
    template_name = 'tournaments.html'
    context_object_name = 'tournaments'

class TournamentDetailView(DetailView):
    model = Tournament
    template_name = 'tournament_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        tournament = self.get_object()
        game_mode = None

        if tournament.game_mode_type and tournament.game_mode_id:
            game_mode = tournament.game_mode_type.get_object_for_this_type(id=tournament.game_mode_id)

        context['game_mode'] = game_mode
        return context

class TeamDetailView(DetailView):
    model = Team
    template_name = 'team_detail.html'
    context_object_name = 'team'

class PlayerDetailView(DetailView):
    model = Players
    template_name = 'player_detail.html'
    context_object_name = 'player'
