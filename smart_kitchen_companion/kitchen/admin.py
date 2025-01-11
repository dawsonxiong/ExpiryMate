# kitchen/admin.py

from django.contrib import admin
from .models import FoodItem, Inventory

admin.site.register(FoodItem)
admin.site.register(Inventory)
