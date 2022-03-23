"""meml URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
drug_class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('drug_detail/<int:id>', views.drug_detail, name='drug_detail'),
    path('login', views.user_login, name='login'),
    path('logout', views.user_logout, name='logout'),
    path('dashboard', views.dashboard, name='dashboard'),

    path('food', views.food, name='food'),
    path('add_food', views.add_food, name='add_food'),
    path('edit_food/<int:id>', views.edit_food, name='edit_food'),
    path('delete_food/<int:id>', views.delete_food, name='delete_food'),

    path('drug_class', views.drug_class, name='drug_class'),
    path('add_drug_class', views.add_drug_class, name='add_drug_class'),
    path('edit_drug_class/<int:id>', views.edit_drug_class, name='edit_drug_class'),
    path('delete_drug_class/<int:id>',
         views.delete_drug_class, name='delete_drug_class'),

    path('drug', views.drug, name='drug'),
    path('add_drug', views.add_drug, name='add_drug'),
    path('view_drug/<int:id>', views.view_drug, name='view_drug'),
    path('edit_drug/<int:id>', views.edit_drug, name='edit_drug'),
    path('delete_drug/<int:id>',
         views.delete_drug, name='delete_drug'),

    path('add_drug_reaction/<int:id>',
         views.add_drug_reaction, name='add_drug_reaction'),
    path('edit_drug_reaction/<int:id>',
         views.edit_drug_reaction, name='edit_drug_reaction'),
    path('delete_drug_reaction/<int:id>',
         views.delete_drug_reaction, name='delete_drug_reaction'),

    path('add_drug_interaction/<int:id>',
         views.add_drug_interaction, name='add_drug_interaction'),
    path('edit_drug_interaction/<int:id>',
         views.edit_drug_interaction, name='edit_drug_interaction'),
    path('delete_drug_interaction/<int:id>',
         views.delete_drug_interaction, name='delete_drug_interaction'),

    path('add_drug_food_reaction/<int:id>',
         views.add_drug_food_reaction, name='add_drug_food_reaction'),
    path('edit_drug_food_reaction/<int:id>',
         views.edit_drug_food_reaction, name='edit_drug_food_reaction'),
    path('delete_drug_food_reaction/<int:id>',
         views.delete_drug_food_reaction, name='delete_drug_food_reaction'),

    path('add_drug_contraindication/<int:id>',
         views.add_drug_contraindication, name='add_drug_contraindication'),
    path('edit_drug_contraindication/<int:id>',
         views.edit_drug_contraindication, name='edit_drug_contraindication'),
    path('delete_drug_contraindication/<int:id>',
         views.delete_drug_contraindication, name='delete_drug_contraindication'),

    path('users', views.users, name='users'),
    path('add_user', views.add_user, name='add_user'),
    path('edit_user/<int:id>', views.edit_user, name='edit_user'),
    path('delete_user/<int:id>',
         views.delete_user, name='delete_user'),

    # path('delete_drug', views.delete_drug, name='Delete Drug'),
    # path('view_drug', views.view_drug, name='View Drug'),
    # path('user_management', views.user_management, name='User Management'),
    # path('add_user', views.add_user, name='Add user'),
    # path('edit_user', views.edit_user, name='Edit user'),
    # path('delete_user', views.delete_user, name='Delete user'),
    # path('users', views.users, name='Users'),
]
