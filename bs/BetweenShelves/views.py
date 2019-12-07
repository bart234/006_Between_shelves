from django.shortcuts import render, redirect
from django.views import View
from BetweenShelves.forms import FormLogin, FormCreateUser
from django.contrib import messages
from django.contrib.auth.models import User
from BetweenShelves.models import UserCfg, Book
from django.contrib.auth import authenticate, login, logout
# Create your views here.

""" ------------------------------------------------ User manipulation ------------------------------------------------"""
class UserEdit(View):
    def get(self, request):
        if User.is_authenticated:
            u  = User.objects.get(username="User11")
            u2 = UserCfg.objects.get(user_id=u.id)
            return render(request, 'user_edit.html', {"user":u,'cfg':u2})
        else:
            messages.warning(request, "Please login ")
            return redirect('Login')
        pass
    def post(self,request):
        pass

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

"""------------------------------------------------ Guest views ------------------------------------------------"""
class OurBooksList(View):
    def get(self, request):
        """List of website books - list of our books and user - just list wit and rating,  
        link to site with all comments to this book """
        #TODO: add  row with sorting option and search , do in in js  without reload
        #TODO: add info " TO check comment and who can borrow it , please log in"
        b = Book.objects.all()
        return render(request, 'guest_ourbookslist.html', {'b':b})

class LookingForBook(View):
    def get(self, request):
        """Looking for book - list with users requests about books , with ratings and  
        link to comment with button i can sell it - which  sen to login /register site
        General - without infor who is looking for"""

        u= UserCfg.objects.select_related().all()
        t =[zz for el in u if el.user_list_to_buy.all().count() > 0 for zz in el.user_list_to_buy.all() ]
        return render(request, 'guest_lookingforbook.html', {'b':t})
        
class BooksToSell(View):
    def get(self, request):
        """List with books to sell from users, with rrating and link to book comments, with button buy  - which send quest to login/register site"""
        u= UserCfg.objects.select_related().all()
        t =[zz for el in u if el.user_list_to_sell.all().count() > 0 for zz in el.user_list_to_sell.all() ]
        return render(request, 'guest_bookstosell.html', {'b':t})


class BookComments(View):
    def get(self,request):
        """site with information about book, all comments, ratings, after login list who hase it, want to read, who borrowing it, who want to sell it"""
        pass



"""------------------------------------------------ Logged user ------------------------------------------------"""
"""------------------------------------------------ User part ------------------------------------------------"""
class MyBooks(View):
    def get(self,request):
        """site with my books which user have, all books """
        pass

class MyForFree(View):
    def get(self,request):
        """site with my books which user want to give for free"""
        pass

class MyWishList(View):
    def get(self,request):
        """site with my books which user have list to buy,"""
        pass

class MySellList(View):
    def get(self,request):
        """site with my books which user have to sell"""
        pass

class MyBookToBorrow(View):
    def get(self,request):
        """site with my books which user list to borrow - with numbers of request to borrow"""
        pass

class MyBookBorrowedSite(View):
    def get(self,request):
        """site with more details about all books which  user want to borrowed, who hase these book, when he should be send it back, who is next in turn,
        confirm  borrow to person i date which he require, ask to change data which he require, confirm when boock willback for you, as for deposit"""
        pass

class MyBookWhichWantToRead(View):
    def get(self,request):
        """site with my books which user have list to read"""
        pass


"""------------------------------------------------ Community part ------------------------------------------------"""
class WeOurBooksList(View):
    def get(self,request):
        """List of all users books, user can move to book site where can add rating,comment, 
        add to wish list, add to want to read list, check who has this book
        """ 
        pass

class WeWantToRead(View):
    def get(self,request):
        """site with book which community want to read , not to buy, if user have book can set it "it borrow" and will get 
        messeges who want to read it and contact to these people"""    
        pass

class WeLookingFor(View):
    def get(self,request):
        """site to show book which community looking for with btn to buy, ask price, send a message, move to comment site"""
        pass

class WeMoveThemOut(View):
    def get(self,request):
        """site to show book which community want to sell with btn to buy, ask price, send a message, move to comment site"""
        pass

class WeReleaseThem(View):
    def get(self,request):
        """site to show books which you can get for free, requirments to get book, send message,  dips for 24h, move to comment site """
        pass


