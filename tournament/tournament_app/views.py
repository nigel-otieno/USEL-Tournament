from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView, TemplateView
from .models import *
from .forms import *
# from .bracket import Bracket
from django.contrib import messages
from django.http import HttpResponseForbidden, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json 

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
def tournament_create(request):
    if request.method == 'POST':
        form = TournamentForm(request.POST, request.FILES)
        if form.is_valid():
            tournament = form.save(commit=False)
            tournament.created_by = request.user
            tournament.save()
            return redirect('tournament_detail', pk=tournament.pk)
    else:
        form = TournamentForm()
    return render(request, 'tournament_create.html', {'form': form})

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

    return render(request, 'tournament_edit.html', {
        'form': form,
        'tournament': tournament
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
        teams = list(tournament.teams.all())

        sort_by = self.request.GET.get('sort', 'name-asc')
        
        if sort_by == 'name-asc':
            teams = sorted(teams, key=lambda t: t.name.lower())
        elif sort_by == 'name-desc':
            teams = sorted(teams, key=lambda t: t.name.lower(), reverse=True)
        elif sort_by == 'score-asc':
            teams = sorted(teams, key=lambda t: (t.score_one or 0) + (t.score_two or 0) + (t.score_three or 0))
        elif sort_by == 'score-desc':
            teams = sorted(teams, key=lambda t: (t.score_one or 0) + (t.score_two or 0) + (t.score_three or 0), reverse=True)
        
        context['tournament'] = tournament
        context['teams'] = teams
        context['sort_by'] = sort_by
        context['round_headers'] = range(1, tournament.rounds + 1)
        return context
class TeamDetailView(DetailView):
    model = Team
    template_name = 'team_detail.html'
    context_object_name = 'team'

class PlayerDetailView(DetailView):
    model = Players
    template_name = 'player_detail.html'
    context_object_name = 'player'

@csrf_exempt
def update_team_score(request):
    if request.method == "POST":
        data = json.loads(request.body)
        team_id = data.get("team_id")
        score_field = data.get("score_field")
        score_value = data.get("score_value")

        try:
            team = Team.objects.get(id=team_id)
            setattr(team, score_field, score_value)
            team.save()
            return JsonResponse({"success": True})
        except Team.DoesNotExist:
            return JsonResponse({"success": False, "error": "Team not found"})
        except Exception as e:
            return JsonResponse({"success": False, "error": str(e)})

    return JsonResponse({"success": False, "error": "Invalid request"})