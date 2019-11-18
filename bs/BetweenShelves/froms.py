from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm
from BetweenShelves.models import UserCfg, Hobby, Genre

HOBBYS = [(el.id,el.types)for el in Hobby.objects.all()]
GENRE = [(el.id,el.types)for el in Genre.objects.all()]

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

class FormEditUser(forms.Form):

    fname = forms.CharField(min_length=2, max_length=20, label='First name', required=False)
    lanme = forms.CharField(min_length=2, max_length=20, label='Last name', required=False)
    email = forms.EmailField(min_length=4, max_length=40, label='Email', required = True)

    description = forms.CharField(widget = forms.Textarea,label='Description',max_length = 300)
    mobile = forms.CharField(label='Mobile', max_length=9, required=False)
    hobby = forms.MultipleChoiceField(choices=HOBBYS, widget=forms.SelectMultiple(), required=False)
    favourite_kind_of_books =forms.ChoiceField(choices=GENRE, widget=forms.SelectMultiple(), required=False)

    pwd_old = forms.CharField(widget=forms.PasswordInput, min_length=4, max_length=20, label='Old password')
    pwd_new1 = forms.CharField(widget=forms.PasswordInput, min_length=4, max_length=20, label='New password')
    pwd_new2 = forms.CharField(widget=forms.PasswordInput, min_length=4, max_length=20, label='Repeat new password')