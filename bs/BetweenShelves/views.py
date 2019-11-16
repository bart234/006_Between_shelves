from django.shortcuts import render, redirect
from django.views import View
from BetweenShelves.froms import FormLogin, FormCreateUser
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
# Create your views here.

class Index(View):
    def get(self,request):
        return render(request, 'index.html')

class Login(View):
    def get(self, request):
        flogin = FormLogin()
        return render(request,'login.html', {'form':flogin})

    def post(self,request):
        form= FormLogin(request.POST)
        if form.is_valid():
            l = form.cleaned_data['username']
            p = form.cleaned_data['pwd']
            user = authenticate(request, username=l, password=p)
            if user is not None:
                login(request, user)
                messages.success(request, "{} login succesful".format(l))
                return redirect('Index') 
                
        messages.warning(request, "Login or password is wrong. Please try again")
        return redirect('Login')
    
class Logout(View):
    def get(self,request):
        logout(request)
        messages.success(request, "You are logged out")
        return redirect("Index")

class CreateUser(View):
    def get(self, request):
        f = FormCreateUser()
        return render(request,'newuser.html', {'form':f})

    def post(self, request):
        pass