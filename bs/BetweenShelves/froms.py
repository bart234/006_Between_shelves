from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm
from BetweenShelves.models import UserCfg

class FormLogin(forms.Form):    
    username = forms.CharField(min_length=4, max_length=20, label='Login', required=True)
    pwd = forms.CharField(widget = forms.PasswordInput, min_length=6, max_length=20, label='Password', required=True)

class FormCreateUser(forms.Form):
    username = forms.CharField(min_length=4, max_length=20, label='Login', required=True)
    pwd1 = forms.CharField(widget=forms.PasswordInput, min_length=4, max_length=20, label='Password', required=True)
    pwd2 = forms.CharField(widget=forms.PasswordInput, min_length=4, max_length=20, label='Repeat password', required=True)
    fname = forms.CharField(min_length=2, max_length=20, label='First name', required=False)
    lanme = forms.CharField(min_length=2, max_length=20, label='Last name', required=False)
    email = forms.EmailField(min_length=4, max_length=40, label='Email', required = True)
    mobile = forms.CharField(max_length=9, min_length=9, label="Mobile", required=False)
