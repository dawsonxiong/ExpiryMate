from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('inventory/', views.inventory, name='inventory'),
    path('register/', views.register, name='register'),
    path('remove_item/<int:item_id>/', views.remove_item, name='remove_item'),
]
