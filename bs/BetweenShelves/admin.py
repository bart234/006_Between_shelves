from django.contrib import admin
from .models import Genre, SubGenre, Book, Hobby, UserCfg
# Register your models here.
admin.site.register(Genre)
admin.site.register(SubGenre)
admin.site.register(Book)
admin.site.register(Hobby)
admin.site.register(UserCfg)