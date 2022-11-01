from django.shortcuts import render, redirect

from notes.web.forms import AddUserForm, AddNoteForm, EditNoteForm, DeleteNoteForm
from notes.web.models import Profile, Note


# Create your views here.


def get_profile():
    try:
        return Profile.objects.get()
    except Profile.DoesNotExist as ex:
        return None


def context_with_profile():
    profile = get_profile()
    context = {'profile': profile}
    return context


def index(request):
    profile = get_profile()
    context = {'profile': profile}
    notes = Note.objects.all()
    if request.method == 'GET':
        form = AddUserForm()
    else:
        form = AddUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    context['form'] = form
    context['notes'] = notes
    if profile:
        return render(request, 'core/home-with-profile.html', context)
    else:
        return render(request, 'core/home-no-profile.html', context)


def add_note(request):
    context = context_with_profile()
    if request.method == 'GET':
        form = AddNoteForm()
    else:
        form = AddNoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    context['form'] = form
    return render(request, 'note/note-create.html', context)


def edit_note(request, pk):
    note = Note.objects.filter(pk=pk).get()
    context = context_with_profile()
    if request.method == 'GET':
        form = EditNoteForm(instance=note)
    else:
        form = EditNoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect('index')
    context['form'] = form
    context['note'] = note
    return render(request, 'note/note-edit.html', context)


def delete_note(request, pk):
    note = Note.objects.filter(pk=pk).get()
    context = context_with_profile()
    if request.method == 'GET':
        form = DeleteNoteForm(instance=note)
    else:
        form = DeleteNoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect('index')
    context['form'] = form
    context['note'] = note

    return render(request, 'note/note-delete.html', context)


def details_note(request, pk):
    context = context_with_profile()
    note = Note.objects.filter(pk=pk).get()
    context['note'] = note
    return render(request, 'note/note-details.html', context)


def profile_details(request):
    context = context_with_profile()
    notes_count = Note.objects.count()
    context['notes_count'] = notes_count
    return render(request, 'profile/profile.html', context)


def delete_profile(request):
    profile = get_profile()
    notes = Note.objects.all()
    notes.delete()
    profile.delete()
    return redirect('index')
