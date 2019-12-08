from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

# Create your models here.
class Genre(models.Model):
    types = models.CharField(max_length = 100, null=False)
    status = models.IntegerField(null=False)

    def __str__(self):
        return self.types

class Book(models.Model):
    title = models.CharField(max_length = 250, null=False, unique=True)
    author = models.CharField(max_length = 150, null=True)
    genre = models.ForeignKey(Genre, on_delete=models.PROTECT, null=False)
    subgenre = models.ForeignKey(Genre, on_delete=models.PROTECT, null=True, related_name='subgenre')
    heigth = models.IntegerField(null=True)
    price = models.DecimalField(max_digits=5, decimal_places=2, null=False)
    comment = models.CharField(max_length = 500, null = True, default ="")
    rating = models.DecimalField(max_digits=2, decimal_places=1, null=True, default = 0.0)


    def __str__(self):
        return self.title

class Hobby(models.Model):
    types = models.CharField(max_length = 100, null=False)
    status = models.IntegerField(null=False)

    def __str__(self):
        return self.types

class Borrows(models.Model):
    user_who_posses = models.OneToOneField(User,unique = True, blank=False, related_name ='user_who_posses',on_delete=models.PROTECT)
    user_who_borrow = models.OneToOneField(User,unique = True, blank=False, related_name ='user_who_borrow',on_delete=models.PROTECT)
    book = models.OneToOneField(Book,unique = True, blank=False, related_name ='book_name',on_delete=models.PROTECT)   

    deposit = models.CharField(null=False, max_length = 300)    
    deposit_recive = models.BooleanField(null=False, default=False)
    deposit_recive_date= models.DateTimeField( null=True)
    deposit_back = models.BooleanField(null=False, default=False)
    deposit_back_recive_date = models.DateTimeField(null=True)

    send_book_date_posses =models.DateTimeField( null=True)
    recive_date_borrow =models.DateTimeField( null=True)
    borrow_duration = models.IntegerField (null=False)
    back_send_date_borrow =models.DateTimeField( null=True)
    back_recive_date_posses =models.DateTimeField( null=True)
    
    borrow_comment = models.CharField(null=True, max_length=300)


class UserCfg(models.Model):
    user = models.OneToOneField(User,unique = True, blank=False, on_delete=models.CASCADE)
    description = models.CharField(null=True, max_length = 300)
    mobile = models.CharField(null=False, max_length=9)
    hobby = models.ManyToManyField(Hobby, blank=True, related_name='hobby')
    favourite_books = models.ManyToManyField(Book, blank=True, related_name= 'fav_books')
    favourite_kind_of_books = models.ManyToManyField(Genre,  blank=True,related_name='fav_kind_of_bboks')
    user_books = models.ManyToManyField(Book, blank=True, related_name='user_books')
    user_list_to_buy  = models.ManyToManyField(Book, blank=True, related_name='user_buy')
    user_list_to_sell = models.ManyToManyField(Book,  blank=True,related_name='user_sell')
    user_list_to_lend = models.ManyToManyField(Book,  blank=True,related_name='user_b_lend_for_others')
    user_list_to_borrow = models.ManyToManyField(Book,  blank=True,related_name='user_b_borrow_to_others')
    user_borrowed_b = models.ManyToManyField(Borrows, blank=True, related_name='borrowed_books')
    friends = models.ManyToManyField(User, blank=True, related_name='friends')
    
    def __str__(self):
        return self.user.username



class Comments(models.Model):
    user = models.ForeignKey(User, null = False, on_delete=models.PROTECT)
    book = models.ForeignKey(Book, null=False,  on_delete=models.PROTECT)
    create_time = models.DateTimeField(default=datetime.now, null=False)
    comment = models.CharField(null = False, max_length=300)

