from django.shortcuts import render, redirect

from recipes.web.forms import CreateRecipeForm, EditRecipeForm, DeleteRecipeForm
from recipes.web.models import Recipe


# Create your views here.


def index(request):
    recipes = Recipe.objects.all()
    context = {'recipes': recipes}
    return render(request, 'index.html', context)


def create(request):
    if request.method == "GET":
        form = CreateRecipeForm()
    else:
        form = CreateRecipeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    context = {'form': form, }
    return render(request, 'create.html', context)


def edit(request, pk):
    recipe = Recipe.objects.filter(pk=pk).get()
    if request.method == "GET":
        form = EditRecipeForm(instance=recipe)
    else:
        form = EditRecipeForm(request.POST, instance=recipe)
        if form.is_valid():
            form.save()
            return redirect('index')
    context = {'form': form, 'recipe': recipe}
    return render(request, 'edit.html', context)


def delete(request, pk):
    recipe = Recipe.objects.filter(pk=pk).get()
    if request.method == "GET":
        form = DeleteRecipeForm(instance=recipe)
    else:
        form = DeleteRecipeForm(request.POST, instance=recipe)
        if form.is_valid():
            form.save()
            return redirect('index')
    context = {'form': form, 'recipe': recipe}
    return render(request, 'delete.html', context)


def details(request, pk):
    recipe = Recipe.objects.filter(pk=pk).get()
    ingredients_list = list(recipe.ingredients.split(','))
    while '' in ingredients_list:
        ingredients_list.remove('')
    context = {'recipe': recipe, 'ingredients_list': ingredients_list}
    return render(request, 'details.html', context)
