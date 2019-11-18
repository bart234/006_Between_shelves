
from django.contrib import admin
from django.urls import path
from BetweenShelves.views import Index, Login, Logout, CreateUser, UserEdit

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Index.as_view(), name='Index'),
    path('login/',Login.as_view() , name ='Login'),
    path('logout/', Logout.as_view(), name='Logout'),
    path('signin/', CreateUser.as_view(), name="CreateUser"),
    path('edituser/', UserEdit.as_view(), name="UserEdit"),
]
