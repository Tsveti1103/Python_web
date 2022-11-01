from django.shortcuts import render, redirect

from GamesPlay.games.forms import ProfileCreateForm, GameCreateForm, GameEditForm, GameDeleteForm, ProfileEditForm, \
    ProfileDeleteForm
from GamesPlay.games.models import Game, Profile


# Create your views here.
def get_profile():
    try:
        profile = Profile.objects.all()
        if profile:
            return profile[0]
    except Profile.DoesNotExist as ex:
        return None


def index(request):
    profile = get_profile()
    context = {'profile': profile}
    return render(request, 'core/home-page.html', context)


def dashboard(request):
    games = Game.objects.all()
    profile = get_profile()
    context = {'games': games, 'profile': profile}
    return render(request, 'core/dashboard.html', context)


def create_game(request):
    profile = get_profile()
    if request.method == 'GET':
        form = GameCreateForm()
    else:
        form = GameCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    context = {'form': form, 'profile': profile}
    return render(request, 'game/create-game.html', context)


def delete_game(request, pk):
    game = Game.objects.filter(pk=pk).get()
    profile = get_profile()
    if request.method == "GET":
        form = GameDeleteForm(instance=game)
    else:
        form = GameDeleteForm(request.POST, instance=game)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    context = {
        'form': form,
        'game': game,
        'profile': profile
    }
    return render(request, 'game/delete-game.html', context)


def details_game(request, pk):
    game = Game.objects.filter(pk=pk).get()
    profile = get_profile()
    context = {'game': game, 'profile': profile}
    return render(request, 'game/details-game.html', context)


def edit_game(request, pk):
    game = Game.objects.filter(pk=pk).get()
    profile = get_profile()
    if request.method == "GET":
        form = GameEditForm(instance=game)
    else:
        form = GameEditForm(request.POST, instance=game)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    context = {
        'form': form,
        'game': game,
        'profile': profile
    }
    return render(request, 'game/edit-game.html', context)


def create_profile(request):
    profile = get_profile()
    if request.method == 'GET':
        form = ProfileCreateForm()
    else:
        form = ProfileCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    context = {
        'form': form,
        'profile': profile, }
    return render(request, 'profile/create-profile.html', context)


def delete_profile(request):
    profile = get_profile()
    if request.method == 'GET':
        form = ProfileDeleteForm(instance=profile)
    else:
        form = ProfileDeleteForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('index')
    context = {
        'form': form,
        'profile': profile
    }
    return render(request, 'profile/delete-profile.html', context)


def details_profile(request):
    profile = get_profile()
    games = Game.objects.all()
    games_count = games.count()
    average_rating = sum([g.rating for g in games]) / games_count if games_count > 0 else 0
    context = {
        'profile': profile,
        'games_count': games_count,
        'average_rating': average_rating
    }
    return render(request, 'profile/details-profile.html', context)


def edit_profile(request):
    profile = get_profile()

    if request.method == 'GET':
        form = ProfileEditForm(instance=profile)
    else:
        form = ProfileEditForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('details profile')
    context = {'form': form, 'profile': profile}
    return render(request, 'profile/edit-profile.html', context)
