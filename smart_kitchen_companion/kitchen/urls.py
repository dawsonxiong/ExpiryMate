from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('inventory/', views.inventory, name='inventory'),
    path('register/', views.register, name='register'),
    path('remove_item/<int:item_id>/', views.remove_item, name='remove_item'),
    path('edit_item/<int:item_id>/', views.edit_item, name='edit_item'),
    path('recipes/', views.recipe_suggestions, name='recipe_suggestions'),
]
