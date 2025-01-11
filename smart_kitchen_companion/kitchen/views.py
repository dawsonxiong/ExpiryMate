# kitchen/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import FoodItemForm
from .models import Inventory, FoodItem
from django.contrib import messages
from .forms import UserRegistrationForm
from django.http import HttpResponseRedirect
from django.urls import reverse
import random


def home(request):
    context = {}
    if request.user.is_authenticated:
        user_inventory, created = Inventory.objects.get_or_create(user=request.user)
        items = user_inventory.items.all()
        context['items'] = items
    return render(request, 'kitchen/home.html', context)


@login_required(login_url='login')
def inventory(request):
    user_inventory, created = Inventory.objects.get_or_create(user=request.user)
    items = user_inventory.items.all()

    if request.method == 'POST':
        form = FoodItemForm(request.POST)
        if form.is_valid():
            food_item = form.save(commit=False)
            food_item.user = request.user
            food_item.save()
            user_inventory.items.add(food_item)
            return redirect('inventory')
    else:
        form = FoodItemForm()

    context = {
        'items': items,
        'form': form
    }
    return render(request, 'kitchen/inventory.html', context)

@login_required(login_url='login')
def remove_item(request, item_id):
    if request.method == 'POST':
        food_item = get_object_or_404(FoodItem, id=item_id, user=request.user)
        user_inventory = Inventory.objects.get(user=request.user)
        user_inventory.items.remove(food_item)
        food_item.delete()
        return HttpResponseRedirect(reverse('inventory'))

@login_required(login_url='login')
def edit_item(request, item_id):
    food_item = get_object_or_404(FoodItem, id=item_id, user=request.user)
    if request.method == 'POST':
        form = FoodItemForm(request.POST, instance=food_item)
        if form.is_valid():
            form.save()
            return redirect('inventory')
    else:
        form = FoodItemForm(instance=food_item)

    return render(request, 'kitchen/edit_item.html', {'form': form, 'item': food_item})


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}. You can now log in.')
            return redirect('login')
    else:
        form = UserRegistrationForm()
    return render(request, 'kitchen/register.html', {'form': form})


def recipe_suggestions(request):
    if request.user.is_authenticated:
        user_inventory = Inventory.objects.get(user=request.user)
        items = user_inventory.items.all()

        # Mock recipe list (replace this with AI-generated recipes later)
        mock_recipes = [
            {"name": "Pasta Primavera", "ingredients": ["pasta", "vegetables", "olive oil"]},
            {"name": "Chicken Stir Fry", "ingredients": ["chicken", "vegetables", "soy sauce"]},
            {"name": "Vegetable Soup", "ingredients": ["vegetables", "broth", "herbs"]},
            {"name": "Fruit Salad", "ingredients": ["apple", "banana", "orange"]},
            {"name": "Omelette", "ingredients": ["eggs", "cheese", "vegetables"]},
        ]
        # Filter recipes based on available ingredients (simple matching for now)
        available_ingredients = [item.name.lower() for item in items]
        suggested_recipes = []
        for recipe in mock_recipes:
            if any(ingredient in available_ingredients for ingredient in recipe['ingredients']):
                suggested_recipes.append(recipe)

        # If no matches, suggest random recipes
        if not suggested_recipes:
            suggested_recipes = random.sample(mock_recipes, min(3, len(mock_recipes)))

        context = {
            'recipes': suggested_recipes,
            'inventory_items': items
        }
        return render(request, 'kitchen/recipe_suggestions.html', context)
    else:
        return redirect('login')



