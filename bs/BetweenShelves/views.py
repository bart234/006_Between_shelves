from django.shortcuts import render, redirect
from django.views import View
from BetweenShelves.froms import FormLogin, FormCreateUser
from django.contrib import messages
from django.contrib.auth.models import User
from BetweenShelves.models import UserCfg
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
        return render(request,'user_new.html', {'form':f})

    def post(self, request):
        form = FormCreateUser(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            p1 = form.cleaned_data['pwd1']
            p2 = form.cleaned_data['pwd2']
            fname = form.cleaned_data['fname']
            lname = form.cleaned_data['lanme']
            email = form.cleaned_data['email']
            mobile = form.cleaned_data['mobile']
            u = User()
            u.username = username
            if p1 == p2:
                u.set_password(p1)
            else:
                messages.warning(request, "Login or password is wrong. Please try again")
                return redirect('Login')
            u.first_name = fname
            u.last_name = lname
            u.email = email
            u.save()
            cfg = UserCfg(user=u,mobile=mobile)
            cfg.save()
            messages.success(request, "Account created, You can log in now")
            return redirect('Login')


        else:
            messages.warning(request, "Login or password is wrong. Please try again")
            return redirect('Login')