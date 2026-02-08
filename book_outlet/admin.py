from django.contrib import admin

from .models import Book
# Register your models here.

admin.site.register(Book) # Le dice que quiero administrar este model a traves de la admin interface.