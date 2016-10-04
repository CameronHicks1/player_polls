from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from django.contrib.auth import authenticate, login, logout
from player_polls.models import Team, Player, Comment
from django.contrib.auth.models import User
from django.db import IntegrityError
import datetime


class IndexView(generic.ListView):
    template_name = 'player_polls/index.html'
    context_object_name = 'teams'

    def get_queryset(self):
        return Team.objects.order_by('name')[:30]


class DetailView(generic.DetailView):
    model = Team, Player
    template_name = 'player_polls/detail.html'

    def get_queryset(self):
        return Team.objects


class ResultsView(generic.DetailView):
    model = Team, Player
    template_name = 'player_polls/results.html'
    
    def get_object(self):
        return Player.objects.get(pk=self.kwargs['slug'])

    def get_queryset(self):
        return Player.objects.order_by('post_date')[:5]


class HomeView(generic.DetailView):
    model = Team, Player, Comment
    template_name = 'player_polls/home.html/'


def login_page_view(request):
    return render(request, 'player_polls/login.html')


def team_view(request, team_id):
    team = get_object_or_404(Team, pk=team_id)
    try:
        players = team.choice_set.get(pk=request.POST['player'])
    except (KeyError, Player.DoesNotExist):
        return render(request, 'player_polls/detail.html', {
            'team': team,
            'error_message': "Please select a player.",
        })


def create_user_post(request):
    username = request.POST['username']
    email = request.POST['email']
    password = request.POST['password']

    try:
        if username != "" and email != "" and password != "":
            user = User.objects.create_user(
                username=username,
                email=email,
                password=password,
                )
            return render(request, 'player_polls/login.html')
        
        elif User.objects.filter(username=username).exists():
            return render(request, 'player_polls/create.html', {
                'error_message': "User already exists",
            })
        
        else:
            return render(request, 'player_polls/create.html', {
                'error_message': "Invalid Credentials",
            })
        
    except IntegrityError:
        return render(request, 'player_polls/create.html', {
                'error_message': "Username already taken",
            })


def user_profile_view(request):
    return render(request, 'player_polls/home.html')


def create_account_view(request):
    return render(request, 'player_polls/create.html')


def login_view(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)

    if user is not None:
        login(request, user)
        return render(request,'player_polls/home.html')

    else:
        return render(request, 'player_polls/login.html', {
            'error_message': "Invalid Login",
        })


def logout_view(request):
    logout(request)

    return (render(request, 'player_polls/login.html'))


def comment_view(request, player_id):
    comment = request.POST['user_comment']
    player = get_object_or_404(Player, pk=player_id)
    user = request.user
    post_time = datetime.datetime.now()    

    try:
        new_comment = Comment(player=player, text=comment, user=user, post_date=post_time)
        player.comment_count += 1
        player.save()
        new_comment.save()

    except (KeyError, Player.DoesNotExist):
        "Error: Player does not exist"

    return (render(request, 'player_polls/home.html'))
