# kitchen/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import FoodItemForm
from .models import Inventory, FoodItem
from django.contrib import messages
from .forms import UserRegistrationForm
from django.http import HttpResponseRedirect
from django.urls import reverse


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
