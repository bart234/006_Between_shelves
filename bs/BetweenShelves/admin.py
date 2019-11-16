from django.contrib import admin
from .models import Genre,  Book, Hobby, UserCfg
# Register your models here.
admin.site.register(Genre)
admin.site.register(Book)
admin.site.register(Hobby)
admin.site.register(UserCfg)