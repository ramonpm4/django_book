from django.contrib import admin

from .models import Book
# Register your models here.

class BookAdmin(admin.ModelAdmin): # Configura administration for the Book model.
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Book, BookAdmin) # Le dice que quiero administrar este model a traves de la admin interface.