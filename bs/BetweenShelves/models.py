from django.db import models
from django.contrib.auth.models import User

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

    def __str__(self):
        return self.title

class Hobby(models.Model):
    types = models.CharField(max_length = 100, null=False)
    status = models.IntegerField(null=False)

    def __str__(self):
        return self.types


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
    friends = models.ManyToManyField(User, blank=True, related_name='friends')

    def __str__(self):
        return self.user.username