from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404

from .models import Book

# Create your views here.

def index(request) -> HttpResponse:
    books = Book.objects.all()
    return render(request, 'book_outlet/index.html', {
        'books': books
    })
    

def book_detail(request, id) -> HttpResponse:
    # try: 
    #     book = Book.objects.get(pk=id) # pk: primary key
    # except:
    #     raise Http404()
    
    book = get_object_or_404(Book, pk=id) # Es lo mismo que lo de arriba.
    return render(request, 'book_outlet/book_detail.html', {
        'title': book.title,
        'author': book.author,
        'rating': book.rating,
        'is_bestseller': book.is_best_selling
    })