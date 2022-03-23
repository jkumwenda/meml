from multiprocessing.sharedctypes import Value
from django import forms
from django.forms import CharField, EmailField, ModelForm, TextInput, Select, Textarea
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SearchForm(forms.Form):
    search = forms.CharField(label='',
                             widget=forms.TextInput(attrs={'class': 'form-control form-control-lg search-input', 'placeholder': 'Drug name...'}))


class LoginForm(forms.Form):
    username = forms.CharField(label='',
                               widget=forms.TextInput(attrs={'class': 'form-control form-control-lg', 'placeholder': 'Enter your username'}))

    password = forms.CharField(label='',
                               widget=forms.PasswordInput(attrs={'class': 'form-control form-control-lg', 'placeholder': 'Please enter password'}))


class FoodForm(ModelForm):
    class Meta:
        model = Food
        fields = ("food",)
        widgets = {
            'food': TextInput(attrs={'class': 'form-control'}),
        }


class DrugClassForm(ModelForm):
    class Meta:
        model = DrugClass
        fields = ("drug_class",)
        widgets = {
            'drug_class': TextInput(attrs={'class': 'form-control'}),
        }


class DrugForm(ModelForm):
    class Meta:
        model = Drug
        fields = ("drug_name", "drug_class", "dosage", "manufacturer")
        widgets = {
            'drug_name': TextInput(attrs={'class': 'form-control'}),
            'drug_class': Select(attrs={'class': 'form-control'}),
            'dosage': Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'manufacturer': TextInput(attrs={'class': 'form-control'}),
        }


class DrugReactionForm(ModelForm):

    class Meta:
        model = DrugReaction
        fields = ("drug_reaction",)
        widgets = {
            'drug_reaction': Textarea(attrs={'class': 'form-control', 'rows': 4}),
        }


class DrugInteractionForm(ModelForm):

    class Meta:
        model = DrugInteraction
        fields = ("drug_two", "drug_reaction",)
        widgets = {
            'drug_two': Select(attrs={'class': 'form-control'}),
            'drug_reaction': Textarea(attrs={'class': 'form-control', 'rows': 4}),
        }


class DrugFoodReactionForm(ModelForm):

    class Meta:
        model = DrugFoodReaction
        fields = ("food", "drug_food_reaction",)
        widgets = {
            'food': Select(attrs={'class': 'form-control'}),
            'drug_food_reaction': Textarea(attrs={'class': 'form-control', 'rows': 4}),
        }


class DrugContraindicationForm(ModelForm):

    class Meta:
        model = DrugContraindication
        fields = ("drug_contraindication",)
        widgets = {
            'drug_contraindication': Textarea(attrs={'class': 'form-control', 'rows': 4}),
        }


class CreateUserForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control'}), max_length=32)
    first_name = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control'}), max_length=32)
    last_name = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control'}), max_length=32)
    email = forms.CharField(widget=forms.EmailInput(
        attrs={'class': 'form-control'}), max_length=64, help_text='Enter a valid email address')
    password1 = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'Password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'Password Again'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name',
                  'email', 'password1', 'password2', )
