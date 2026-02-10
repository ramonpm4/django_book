from django.contrib import admin

from .models import Book, Author, Adress
# Register your models here.

class BookAdmin(admin.ModelAdmin): # Configura administration for the Book model.
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('author', 'rating')
    list_display = ('title', 'author')
      

admin.site.register(Book, BookAdmin) # Le dice que quiero administrar este model a traves de la admin interface.
admin.site.register(Author)
admin.site.register(Adress)