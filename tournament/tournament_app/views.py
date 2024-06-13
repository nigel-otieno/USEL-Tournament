from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView, TemplateView
from .models import *
from .forms import *
# from .bracket import Bracket
from django.contrib import messages
from django.http import HttpResponseForbidden

@login_required
def tournament_delete(request, tournament_id):
    tournament = get_object_or_404(Tournament, id=tournament_id)
    if request.user != tournament.created_by:
        messages.error(request, "You do not have permission to delete this tournament.")
        return redirect('tournament_detail', tournament_id=tournament.id)
    
    if request.method == 'POST':
        tournament.delete()
        messages.success(request, "Tournament deleted successfully.")
        return redirect('tournaments')
    
    return render(request, 'tournament_confirm_delete.html', {'tournament': tournament})

@login_required
def game_mode_edit(request, tournament_id):
    tournament = get_object_or_404(Tournament, id=tournament_id)
    game_mode = tournament.game_mode

    if isinstance(game_mode, TimeBasedGameMode):
        form_class = TimeBasedGameModeForm
    elif isinstance(game_mode, ScoreBasedGameMode):
        form_class = ScoreBasedGameModeForm
    elif isinstance(game_mode, HybridGameMode):
        form_class = HybridGameModeForm
    else:
        raise ValueError("Unknown game mode")

    if request.method == 'POST':
        form = form_class(request.POST, instance=game_mode)
        if form.is_valid():
            form.save()
            return redirect('tournament_detail', pk=tournament.pk)  # Use pk here
    else:
        form = form_class(instance=game_mode)

    return render(request, 'game_mode_edit.html', {'form': form, 'tournament': tournament})


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


# def bracket_create(request, tournament_id):
#     tournament = get_object_or_404(Tournament, id=tournament_id)
#     if request.method == 'POST':
#         form = BracketForm(request.POST)
#         if form.is_valid():
#             bracket = form.save(commit=False)
#             bracket.tournament = tournament
#             bracket.save()
#             form.save_m2m()
#             return redirect('tournament_detail', tournament.id)
#     else:
#         form = BracketForm()
#     return render(request, 'bracket_create.html', {'form': form, 'tournament': tournament})


# # views.py
# def bracket_display(request, tournament_id):
#     tournament = get_object_or_404(Tournament, id=tournament_id)
#     bracket = get_object_or_404(Bracket, tournament=tournament)
#     return render(request, 'bracket_display.html', {'bracket': bracket, 'tournament': tournament})

@login_required
def tournament_edit(request, id):
    tournament = get_object_or_404(Tournament, id=id)

    if request.user != tournament.created_by:
        return redirect('tournament_detail', pk=tournament.id)

    game_mode_instance = None
    GameModeForm = None

    if hasattr(tournament, 'timebasedgamemode'):
        game_mode_instance = tournament.timebasedgamemode
        GameModeForm = TimeBasedGameModeForm
    elif hasattr(tournament, 'scorebasedgamemode'):
        game_mode_instance = tournament.scorebasedgamemode
        GameModeForm = ScoreBasedGameModeForm
    elif hasattr(tournament, 'hybridgamemode'):
        game_mode_instance = tournament.hybridgamemode
        GameModeForm = HybridGameModeForm

    if request.method == 'POST':
        form = TournamentForm(request.POST, request.FILES, instance=tournament)
        if game_mode_instance:
            game_mode_form = GameModeForm(request.POST, instance=game_mode_instance)
        else:
            game_mode_form = None

        if form.is_valid() and (game_mode_form is None or game_mode_form.is_valid()):
            form.save()
            if game_mode_form:
                game_mode_form.save()
            return redirect('tournament_detail', pk=tournament.id)
    else:
        form = TournamentForm(instance=tournament)
        if game_mode_instance:
            game_mode_form = GameModeForm(instance=game_mode_instance)
        else:
            game_mode_form = None

    return render(request, 'tournament_edit.html', {
        'form': form,
        'tournament': tournament,
        'game_mode_form': game_mode_form
    })

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
    if request.user != team.created_by:
        return HttpResponseForbidden("You are not allowed to upload a video for this team.")

    if request.method == 'POST':
        video_url = request.POST.get('video_url')
        team.video_url = video_url
        team.save()
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
        #use to pass through details and render table client side in TournamentDetails
        game_mode_details = {}                              #use to pass through details and render table client side in TournamentDetails

        if tournament.game_mode_type and tournament.game_mode_id:
            game_mode = tournament.game_mode_type.get_object_for_this_type(id=tournament.game_mode_id)
        if isinstance(game_mode, TimeBasedGameMode):
            game_mode_details = {
                'type': 'TimeBased',
                'rounds': game_mode.rounds,
                'time_score': game_mode.time_score
            }
        elif isinstance(game_mode, ScoreBasedGameMode):
            game_mode_details = {
                'type': 'ScoreBased',
                'rounds': game_mode.rounds
            }
        elif isinstance(game_mode, HybridGameMode):
            game_mode_details = {
                'type': 'Hybrid',
                'rounds': game_mode.rounds,
                'time_score': game_mode.time_score
            }

        context['game_mode'] = game_mode
        context['game_mode_details'] = game_mode_details
        context['headers'] = tournament.get_headers() 
        return context

class TeamDetailView(DetailView):
    model = Team
    template_name = 'team_detail.html'
    context_object_name = 'team'

class PlayerDetailView(DetailView):
    model = Players
    template_name = 'player_detail.html'
    context_object_name = 'player'
