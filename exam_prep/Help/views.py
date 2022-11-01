from django.shortcuts import render, redirect

from music.web.forms import ProfileCreateForm, AlbumAddForm, AlbumDeleteForm, ProfileDeleteForm
from music.web.models import Profile, Album


# Create your views here.
# function to get profile if we have one
def get_profile():
    try:
        return Profile.objects.get()
    except Profile.DoesNotExist as ex:
        return None


# Home page with and without profile
def index(request):
    profile = get_profile()
    albums = Album.objects.all()
    if request.method == 'GET':
        form = ProfileCreateForm()
    else:
        form = ProfileCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    context = {
        'form': form,
        "profile": profile,
        'albums': albums}
    if profile:
        return render(request, 'core/home-with-profile.html', context)
    else:
        return render(request, 'core/home-no-profile.html', context)


# simple view with form
def album_add(request):
    if request.method == 'GET':
        form = AlbumAddForm()
    else:
        form = AlbumAddForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    context = {
        'form': form,
    }
    return render(request, 'album/add-album.html', context)


# simple view without form
def album_details(request, pk):
    album = Album.objects.filter(pk=pk).get()
    context = {'album': album}
    return render(request, 'album/album-details.html', context)


# view for edit - fills the fields with current album info
def album_edit(request, pk):
    # need the album to give it to the instance
    album = Album.objects.filter(pk=pk).get()
    if request.method == 'GET':
        form = AlbumAddForm(instance=album)
    else:
        form = AlbumAddForm(request.POST, instance=album)
        if form.is_valid():
            form.save()
            return redirect('index')
    context = {
        'form': form,
        'album': album,
    }
    return render(request, 'album/edit-album.html', context)


# the same as edit view
def album_delete(request, pk):
    album = Album.objects.filter(pk=pk).get()
    if request.method == 'GET':
        form = AlbumDeleteForm(instance=album)
    else:
        form = AlbumDeleteForm(request.POST, instance=album)
        if form.is_valid():
            form.save()
            return redirect('index')
    context = {
        'form': form,
        'album': album,
    }
    return render(request, 'album/delete-album.html', context)


# delete without form but have to put it in urls
def delete_book(request, pk):
    book = Album.objects.get(pk=pk)
    book.delete()
    return redirect('index')


# simple view without form
def profile_details(request):
    profile = get_profile()
    albums_count = Album.objects.count()

    context = {'profile': profile, 'albums_count': albums_count}
    return render(request, 'profile/profile-details.html', context)


# the same as the other delete and edit views
def profile_delete(request):
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
    }
    return render(request, 'profile/profile-delete.html', context)

# delete if don't have form
def delete_profile(request):
    profile = get_profile()
    albums = Album.objects.all()
    albums.delete()
    profile.delete()
    return redirect('index')