from django.shortcuts import render, redirect

from exam.web.forms import ProfileCreateForm, CarCreateForm, CarEditForm, CarDeleteForm, ProfileEditForm, \
    ProfileDeleteForm
from exam.web.models import Profile, Car


def get_profile():
    try:
        return Profile.objects.get()
    except Profile.DoesNotExist as ex:
        return None


def get_profile_in_context():
    profile = get_profile()
    context = {'profile': profile}
    return context


def index(request):
    context = get_profile_in_context()
    return render(request, 'core/index.html', context)


def catalogue(request):
    context = get_profile_in_context()
    if context['profile'] is None:
        return redirect('index')
    cars = Car.objects.all()
    cars_count = Car.objects.count
    context['cars'] = cars
    context['cars_count'] = cars_count
    return render(request, 'core/catalogue.html', context)


def create_car(request):
    context = get_profile_in_context()
    if context['profile'] is None:
        return redirect('index')
    if request.method == 'GET':
        form = CarCreateForm()
    else:
        form = CarCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('catalogue')
    context['form'] = form
    return render(request, 'car/car-create.html', context)


def details_car(request, pk):
    car = Car.objects.filter(pk=pk).get()
    context = get_profile_in_context()
    if context['profile'] is None:
        return redirect('index')
    context['car'] = car
    return render(request, 'car/car-details.html', context)


def edit_car(request, pk):
    context = get_profile_in_context()
    car = Car.objects.filter(pk=pk).get()
    if context['profile'] is None:
        return redirect('index')
    if request.method == 'GET':
        form = CarEditForm(instance=car)
    else:
        form = CarEditForm(request.POST, instance=car)
        if form.is_valid():
            form.save()
            return redirect('catalogue')
    context['form'] = form
    context['car'] = car
    return render(request, 'car/car-edit.html', context)


def delete_car(request, pk):
    context = get_profile_in_context()
    car = Car.objects.filter(pk=pk).get()
    if context['profile'] is None:
        return redirect('index')
    if request.method == 'GET':
        form = CarDeleteForm(instance=car)
    else:
        form = CarDeleteForm(request.POST, instance=car)
        if form.is_valid():
            form.save()
            return redirect('catalogue')
    context['form'] = form
    context['car'] = car
    return render(request, 'car/car-delete.html', context)


def create_profile(request):
    context = get_profile_in_context()
    if request.method == 'GET':
        form = ProfileCreateForm()
    else:
        form = ProfileCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('catalogue')
    context['form'] = form
    return render(request, 'profile/profile-create.html', context)


def details_profile(request):
    context = get_profile_in_context()
    total_price = sum([car.price for car in Car.objects.all()])
    if context['profile'] is None:
        return redirect('index')
    context['total_price'] = total_price
    return render(request, 'profile/profile-details.html', context)


def edit_profile(request):
    context = get_profile_in_context()
    profile = get_profile()
    if context['profile'] is None:
        return redirect('index')
    if request.method == 'GET':
        form = ProfileEditForm(instance=profile)
    else:
        form = ProfileEditForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('details profile')
    context['form'] = form
    return render(request, 'profile/profile-edit.html', context)


def delete_profile(request):
    context = get_profile_in_context()
    profile = get_profile()
    if context['profile'] is None:
        return redirect('index')
    if request.method == 'GET':
        form = ProfileDeleteForm(instance=profile)
    else:
        form = ProfileDeleteForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('index')
    context['form'] = form
    return render(request, 'profile/profile-delete.html', context)
