from django.shortcuts import render, redirect

from library.web.forms import ProfileCreateForm, BookAddForm, BookEditForm, ProfileEditForm, ProfileDeleteForm
from library.web.models import Profile, Book


def get_profile():
    try:
        return Profile.objects.get()
    except Profile.DoesNotExist as ex:
        return None


# Create your views here.
def index(request):
    profile = get_profile()
    books = Book.objects.all()
    if request.method == 'GET':
        form = ProfileCreateForm()
    else:
        form = ProfileCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    context = {
        'form': form,
        'profile': profile,
        'books': books,
    }
    if profile:
        return render(request, 'core/home-with-profile.html', context)
    else:
        return render(request, 'core/home-no-profile.html', context)


def add_book(request):
    if request.method == 'GET':
        form = BookAddForm()
    else:
        form = BookAddForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    context = {'form': form, }
    return render(request, 'book/add-book.html', context)


def edit_book(request, pk):
    book = Book.objects.filter(pk=pk).get()
    if request.method == 'GET':
        form = BookEditForm(instance=book)
    else:
        form = BookEditForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('index')
    context = {'form': form, 'book': book, }
    return render(request, 'book/edit-book.html', context)


def details_book(request, pk):
    book = Book.objects.filter(pk=pk).get()
    context = {'book': book}
    return render(request, 'book/book-details.html', context)


def delete_book(request, pk):
    book = Book.objects.get(pk=pk)
    book.delete()
    return redirect('index')


def details_profile(request):
    profile = get_profile()
    context = {'profile': profile}
    return render(request, 'profile/profile.html', context)


def edit_profile(request):
    profile = get_profile()
    if request.method == 'GET':
        form = ProfileEditForm(instance=profile)
    else:
        form = ProfileEditForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('index')
    context = {'form': form, 'profile': profile}
    return render(request, 'profile/edit-profile.html', context)


def delete_profile(request):
    profile = get_profile()
    if request.method == 'GET':
        form = ProfileDeleteForm(instance=profile)
    else:
        form = ProfileDeleteForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('index')
    context = {'form': form, 'profile': profile}
    return render(request, 'profile/delete-profile.html', context)
