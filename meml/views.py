from .forms import *
from django.shortcuts import redirect
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .forms import *
from .models import *
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
import datetime
from django.utils.timezone import now

# Create your views here.


def index(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            query = form.cleaned_data.get('search')
            drugs = Drug.objects.filter(Q(drug_name__icontains=query))
            if not drugs.count():
                messages.error(request, "Data not found.")
    else:
        form = SearchForm()
        drugs = []
    context = {'drugs': drugs, 'form': form}
    return render(request, 'home/home.html', context)


def drug_detail(request, id):
    drug = Drug.objects.get(drug_id=id)
    drug_reactions = DrugReaction.objects.filter(drug=id)
    drug_interactions = DrugInteraction.objects.filter(drug=id)
    drug_food_reactions = DrugFoodReaction.objects.filter(drug=id)
    drug_contraindications = DrugContraindication.objects.filter(drug=id)

    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            query = form.cleaned_data.get('search')
            drugs = Drug.objects.filter(Q(drug_name__icontains=query))
            if not drugs.count():
                messages.error(request, "Data not found.")
                form = SearchForm()
                drugs = []

            context = {'drugs': drugs, 'form': form}
            return render(request, 'home/home.html', context)
    else:
        form = SearchForm()
    hits = Hits()
    hits.drug = Drug.objects.get(drug_id=id)
    hits.ip_address = request.META.get("REMOTE_ADDR")
    hits.save()
    context = {'page_title': 'Drug details', 'drug': drug, 'drug_reactions': drug_reactions,
               'drug_interactions': drug_interactions, 'drug_food_reactions': drug_food_reactions, 'drug_contraindications': drug_contraindications, 'cancel': 'drug', 'form': form}
    return render(request, 'home/drug_detail.html', context)


def user_login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                # messages.info(request, f"You are now logged in as {username}.")
                return redirect('/dashboard')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    else:
        form = LoginForm()

    context = {'form': form}
    return render(request, 'login/login.html', context)


def user_logout(request):
    logout(request)
    messages.info(request, "You have successfully logged out.")
    return redirect("/login")


@login_required(login_url='/login')
def dashboard(request):
    date = datetime.datetime.today()
    day = date.day
    week = date.strftime("%V")
    month = date.month
    year = date.year

    hits = {}
    hits['day'] = Hits.objects.filter(created_at__day=day)
    hits['week'] = Hits.objects.filter(created_at__week=week)
    hits['month'] = Hits.objects.filter(created_at__month=month)
    hits['year'] = Hits.objects.filter(created_at__year=year)

    labels = ['Home', 'Lake', 'Summer']
    data = [10, 20, 5]

    page_title = "Dashboard"
    return render(request, 'dashboard/dashboard.html', {'page_title': page_title, 'hits': hits, 'labels': labels, 'data': data, 'week': week})


# Food management functions

@login_required(login_url='/login')
def food(request):
    food = Food.objects.all()
    page_title = "Food items"
    return render(request, 'manage/food/index.html', {'page_title': page_title, 'foods': food})


@login_required(login_url='/login')
def add_food(request):
    if request.method == 'POST':
        form = FoodForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Data inserted successfully")
            return HttpResponseRedirect('/food')
        else:
            messages.warning(request, "Data was not inserted")
    else:
        form = FoodForm()

    context = {'page_title': 'Food details', 'form': form, 'cancel': 'food'}
    return render(request, 'manage/food/add_edit.html', context)


@login_required(login_url='/login')
def edit_food(request, id):
    food_id = Food.objects.get(food_id=id)
    form = FoodForm(instance=food_id)

    if request.method == 'POST':
        form = FoodForm(request.POST, instance=food_id)

        if form.is_valid():
            form.save()
            messages.success(request, "Data updated successfully")
            return HttpResponseRedirect('/food')
        else:
            messages.warning(request, "Data was not updated")
    else:
        form = FoodForm()

    context = {'page_title': 'Food details', 'form': form, 'cancel': 'food'}
    return render(request, 'manage/food/add_edit.html', context)


@login_required(login_url='/login')
def delete_food(request, id):
    food_data = Food.objects.get(food_id=id)
    food_data.delete()
    messages.warning(request, "Data was not deleted")
    return HttpResponseRedirect('/food')


# Drug class management functions

@login_required(login_url='/login')
def drug_class(request):
    drug_class = DrugClass.objects.all()
    context = {'page_title': "Drug class items", 'drug_classes': drug_class}
    return render(request, 'manage/drug_class/index.html', context)


@login_required(login_url='/login')
def add_drug_class(request):
    if request.method == 'POST':
        form = DrugClassForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Data inserted successfully")
            return HttpResponseRedirect('/drug_class')
        else:
            messages.warning(request, "Data was not inserted")
    else:
        form = DrugClassForm()

    context = {'page_title': 'Drug class details',
               'form': form, 'cancel': 'drug_class'}
    return render(request, 'manage/drug_class/add_edit.html', context)


@login_required(login_url='/login')
def edit_drug_class(request, id):
    drug_class_id = DrugClass.objects.get(drug_class_id=id)
    form = DrugClassForm(instance=drug_class_id)

    if request.method == 'POST':
        form = DrugClassForm(request.POST, instance=drug_class_id)

        if form.is_valid():
            form.save()
            messages.success(request, "Data updated successfully")
            return HttpResponseRedirect('/drug_class')
        else:
            messages.warning(request, "Data was not updated")
    else:
        form = DrugClassForm()

    context = {'page_title': 'Drug class details',
               'form': form, 'cancel': 'drug_class'}
    return render(request, 'manage/drug_class/add_edit.html', context)


@login_required(login_url='/login')
def delete_drug_class(request, id):
    drug_class_data = DrugClass.objects.get(drug_class_id=id)
    drug_class_data.delete()
    messages.warning(request, "Data was not deleted")
    return HttpResponseRedirect('/drug_class')


# Drug management functions

@login_required(login_url='/login')
def drug(request):
    drugs = Drug.objects.all()
    context = {'page_title': "Drug items", 'drugs': drugs}
    return render(request, 'manage/drug/index.html', context)


@login_required(login_url='/login')
def add_drug(request):
    if request.method == 'POST':
        form = DrugForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Data inserted successfully")
            return HttpResponseRedirect('/drug')
        else:
            messages.warning(request, "Data was not inserted")
    else:
        form = DrugForm()

    context = {'page_title': 'Drug details',
               'form': form, 'cancel': 'drug'}
    return render(request, 'manage/drug/add_edit.html', context)


@login_required(login_url='/login')
def view_drug(request, id):
    drug = Drug.objects.get(drug_id=id)
    drug_reactions = DrugReaction.objects.filter(drug=id)
    drug_interactions = DrugInteraction.objects.filter(drug=id)
    drug_food_reactions = DrugFoodReaction.objects.filter(drug=id)
    drug_contraindications = DrugContraindication.objects.filter(drug=id)

    date = datetime.datetime.today()
    day = date.day
    week = date.strftime("%V")
    month = date.month
    year = date.year

    hits = {}
    hits['day'] = Hits.objects.filter(drug_id=id, created_at__day=day)
    hits['week'] = Hits.objects.filter(drug_id=id, created_at__week=week)
    hits['month'] = Hits.objects.filter(drug_id=id, created_at__month=month)
    hits['year'] = Hits.objects.filter(drug_id=id, created_at__year=year)

    context = {'page_title': 'Drug details', 'drug': drug, 'drug_reactions': drug_reactions,
               'drug_interactions': drug_interactions, 'drug_food_reactions': drug_food_reactions, 'drug_contraindications': drug_contraindications, 'cancel': 'drug', 'hits': hits}
    return render(request, 'manage/drug/drug.html', context)


@login_required(login_url='/login')
def edit_drug(request, id):
    drug_id = Drug.objects.get(drug_id=id)
    form = DrugForm(instance=drug_id)

    if request.method == 'POST':
        form = DrugForm(request.POST, instance=drug_id)

        if form.is_valid():
            form.save()
            messages.success(request, "Data updated successfully")
            return HttpResponseRedirect('/drug')
        else:
            messages.warning(request, "Data was not updated")
    else:
        form = DrugForm()

    context = {'page_title': 'Drug details', 'form': form, 'cancel': 'drug'}
    return render(request, 'manage/drug/add_edit.html', context)


@login_required(login_url='/login')
def delete_drug(request, id):
    drug_data = Drug.objects.get(drug_id=id)
    drug_data.delete()
    messages.warning(request, "Data was not deleted")
    return HttpResponseRedirect('/drug')


# Drug reaction management functions

@login_required(login_url='/login')
def add_drug_reaction(request, id):
    if request.method == 'POST':
        drug_id = DrugReaction(drug_id=id)
        form = DrugReactionForm(request.POST, instance=drug_id)
        if form.is_valid():
            form.save()
            messages.success(request, "Data inserted successfully")
            return redirect(f'/view_drug/{id}')
        else:
            messages.warning(request, "Data was not inserted")
    else:
        form = DrugReactionForm()

    context = {'page_title': 'Drug Interaction details',
               'form': form, 'id': id}
    return render(request, 'manage/drug/drug_reaction/add_edit.html', context)


@login_required(login_url='/login')
def edit_drug_reaction(request, id):
    drug_reaction_id = DrugReaction.objects.get(drug_reaction_id=id)
    form = DrugReactionForm(instance=drug_reaction_id)

    if request.method == 'POST':
        form = DrugReactionForm(request.POST, instance=drug_reaction_id)

        if form.is_valid():
            form.save()
            messages.success(request, "Data updated successfully")
            return redirect(f'/view_drug/{drug_reaction_id.drug_id}')
        else:
            messages.warning(request, "Data was not updated")
    else:
        form = DrugReactionForm()

    context = {'page_title': 'Drug Interaction details',
               'form': form, 'id': drug_reaction_id.drug_id}
    return render(request, 'manage/drug/drug_reaction/add_edit.html', context)


@login_required(login_url='/login')
def delete_drug_reaction(request, id):
    drug_reaction_data = DrugReaction.objects.get(drug_reaction_id=id)
    drug_id = drug_reaction_data.drug_id
    drug_reaction_data.delete()
    messages.warning(request, "Data was not deleted")
    return redirect(f'/view_drug/{drug_id}')


# Drug interaction management functions

@login_required(login_url='/login')
def add_drug_interaction(request, id):
    if request.method == 'POST':
        drug_id = DrugInteraction(drug_id=id)
        form = DrugInteractionForm(request.POST, instance=drug_id)
        if form.is_valid():
            form.save()
            messages.success(request, "Data inserted successfully")
            return redirect(f'/view_drug/{id}')
        else:
            messages.warning(request, "Data was not inserted")
    else:
        form = DrugInteractionForm()

    context = {'page_title': 'Drug Interaction details',
               'form': form, 'id': id}
    return render(request, 'manage/drug/drug_interaction/add_edit.html', context)


@login_required(login_url='/login')
def edit_drug_interaction(request, id):
    drug_interaction_id = DrugInteraction.objects.get(drug_interaction_id=id)
    form = DrugInteractionForm(instance=drug_interaction_id)

    if request.method == 'POST':
        form = DrugInteractionForm(request.POST, instance=drug_interaction_id)

        if form.is_valid():
            form.save()
            messages.success(request, "Data updated successfully")
            return redirect(f'/view_drug/{drug_interaction_id.drug_id}')
        else:
            messages.warning(request, "Data was not updated")
    else:
        form = DrugInteractionForm()

    context = {'page_title': 'Drug Interaction details',
               'form': form, 'id': drug_interaction_id.drug_id}
    return render(request, 'manage/drug/drug_interaction/add_edit.html', context)


@login_required(login_url='/login')
def delete_drug_interaction(request, id):
    drug_interaction_data = DrugInteraction.objects.get(drug_interaction_id=id)
    drug_id = drug_interaction_data.drug_id
    drug_interaction_data.delete()
    messages.warning(request, "Data was not deleted")
    return redirect(f'/view_drug/{drug_id}')


# Drug food reaction management functions

@login_required(login_url='/login')
def add_drug_food_reaction(request, id):
    if request.method == 'POST':
        drug_id = DrugFoodReaction(drug_id=id)
        form = DrugFoodReactionForm(request.POST, instance=drug_id)
        if form.is_valid():
            form.save()
            messages.success(request, "Data inserted successfully")
            return redirect(f'/view_drug/{id}')
        else:
            messages.warning(request, "Data was not inserted")
    else:
        form = DrugFoodReactionForm()

    context = {'page_title': 'Drug Food Reaction details',
               'form': form, 'id': id}
    return render(request, 'manage/drug/drug_food_reaction/add_edit.html', context)


@login_required(login_url='/login')
def edit_drug_food_reaction(request, id):
    drug_food_reaction_id = DrugFoodReaction.objects.get(
        drug_food_reaction_id=id)
    form = DrugFoodReactionForm(instance=drug_food_reaction_id)

    if request.method == 'POST':
        form = DrugFoodReactionForm(
            request.POST, instance=drug_food_reaction_id)

        if form.is_valid():
            form.save()
            messages.success(request, "Data updated successfully")
            return redirect(f'/view_drug/{drug_food_reaction_id.drug_id}')
        else:
            messages.warning(request, "Data was not updated")
    else:
        form = DrugFoodReactionForm()

    context = {'page_title': 'Drug Food Reaction details',
               'form': form, 'id': drug_food_reaction_id.drug_id}
    return render(request, 'manage/drug/drug_food_reaction/add_edit.html', context)


@login_required(login_url='/login')
def delete_drug_food_reaction(request, id):
    drug_food_reaction_data = DrugFoodReaction.objects.get(
        drug_food_reaction_id=id)
    drug_id = drug_food_reaction_data.drug_id
    drug_food_reaction_data.delete()
    messages.warning(request, "Data was not deleted")
    return redirect(f'/view_drug/{drug_id}')


# Drug contraindication management functions

@login_required(login_url='/login')
def add_drug_contraindication(request, id):
    if request.method == 'POST':
        drug_id = DrugContraindication(drug_id=id)
        form = DrugContraindicationForm(request.POST, instance=drug_id)
        if form.is_valid():
            form.save()
            messages.success(request, "Data inserted successfully")
            return redirect(f'/view_drug/{id}')
        else:
            messages.warning(request, "Data was not inserted")
    else:
        form = DrugContraindicationForm()

    context = {'page_title': 'Drug Contraindication details',
               'form': form, 'id': id}
    return render(request, 'manage/drug/drug_contraindication/add_edit.html', context)


@login_required(login_url='/login')
def edit_drug_contraindication(request, id):
    drug_contraindication_id = DrugContraindication.objects.get(
        drug_contraindication_id=id)
    form = DrugContraindicationForm(instance=drug_contraindication_id)

    if request.method == 'POST':
        form = DrugContraindicationForm(
            request.POST, instance=drug_contraindication_id)

        if form.is_valid():
            form.save()
            messages.success(request, "Data updated successfully")
            return redirect(f'/view_drug/{drug_contraindication_id.drug_id}')
        else:
            messages.warning(request, "Data was not updated")
    else:
        form = DrugContraindicationForm()

    context = {'page_title': 'Drug Contraindication details',
               'form': form, 'id': drug_contraindication_id.drug_id}
    return render(request, 'manage/drug/drug_contraindication/add_edit.html', context)


@login_required(login_url='/login')
def delete_drug_contraindication(request, id):
    drug_contraindication_data = DrugContraindication.objects.get(
        drug_contraindication_id=id)
    drug_id = drug_contraindication_data.drug_id
    drug_contraindication_data.delete()
    messages.warning(request, "Data was not deleted")
    return redirect(f'/view_drug/{drug_id}')

# Users management functions


@login_required(login_url='/login')
def users(request):
    users = User.objects.all()
    context = {'page_title': "System Users", 'users': users}
    return render(request, 'manage/users/index.html', context)


@login_required(login_url='/login')
def add_user(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            return HttpResponseRedirect('/users')
    else:
        form = CreateUserForm()
    context = {'page_title': 'User details',
               'form': form}
    return render(request, 'manage/users/add_edit.html', context)


@login_required(login_url='/login')
def edit_user(request, id):
    user_id = User.objects.get(id=id)
    form = CreateUserForm(instance=user_id)

    if request.method == 'POST':
        form = CreateUserForm(request.POST, instance=user_id)

        if form.is_valid():
            form.save()
            messages.success(request, "Data updated successfully")
            return HttpResponseRedirect('/users')
        else:
            messages.warning(request, "Data was not updated")
    else:
        form = CreateUserForm()

    context = {'page_title': 'User details',
               'form': form}
    return render(request, 'manage/users/add_edit.html', context)


@login_required(login_url='/login')
def delete_user(request, id):
    user_data = User.objects.get(id=id)
    user_data.delete()
    messages.warning(request, "Data was not deleted")
    return HttpResponseRedirect('/users')
