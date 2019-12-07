
from django.contrib import admin
from django.urls import path,re_path
from BetweenShelves.views import Index, Login, Logout, CreateUser, UserEdit, OurBooksList, LookingForBook, BooksToSell
from BetweenShelves.views import BookDetails
from BetweenShelves.views import WeLookingFor,WeMoveThemOut,WeReleaseThem,WeWantToRead
from BetweenShelves.views import MyBooks,MyWishList,MySellList,MyBookToBorrow,MyBookBorrowedSite,MyBookWhichWantToRead,MyForFree
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Index.as_view(), name='Index'),
    path('login/',Login.as_view() , name ='Login'),
    path('logout/', Logout.as_view(), name='Logout'),
    path('signin/', CreateUser.as_view(), name="CreateUser"),
    path('edituser/', UserEdit.as_view(), name="UserEdit"),

    path('books_list/', OurBooksList.as_view(), name ="OurBooksList"),
    path('books_to_buy/', LookingForBook.as_view(), name ="LookingForBook"),
    path('books_to_sell/', BooksToSell.as_view(), name ="BooksToSell"),

    re_path(r'book/(?P<id>(\d){1,6})$',BookDetails.as_view(), name="BookComments"),

    # re_path(r'mylibrary/<str:login>', MyLibrary.as_view(), name="MyLibrary"),
    # re_path(r'mylibrary/<str:login>', MyLibrary.as_view(), name="MyLibrary"),
    path('wewanttoread/', WeWantToRead.as_view(), name="WeWantToRead"),
    path('welookingfor/', WeLookingFor.as_view(), name="WeLookingFor"),
    path('wemovethemout/', WeMoveThemOut.as_view(), name="WeMoveThemOut"),
    path('releasethem/', WeReleaseThem.as_view(), name="WeReleaseThem"),

    path('mybooks/', MyBooks.as_view(), name="MyBooks"),
    path('mywishlist/', MyWishList.as_view(), name="MyWishList"),
    path('myselllist/', MySellList.as_view(), name="MySellList"),
    path('myforfree/', MyForFree.as_view(), name="MyForFree"),
    path('mybooktoborrow/', MyBookToBorrow.as_view(), name="MyBookToBorrow"),
    path('mybookborrowed/', MyBookBorrowedSite.as_view(), name="MyBookBorrowedSite"),
    path('mybookwishread/', MyBookWhichWantToRead.as_view(), name="MyBookWhichWantToRead"),

]

