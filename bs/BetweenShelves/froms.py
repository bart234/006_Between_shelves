from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm

class FormLogin(forms.Form):    
    login = forms.CharField(min_length=4, max_length=20, label='Login', required=True)
    pwd = forms.CharField(min_length=4, max_length=100, label='Password', required=True)