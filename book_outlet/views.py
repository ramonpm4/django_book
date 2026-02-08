from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404
from django.db.models import Avg, Max, Min

from .models import Book

# Create your views here.

def index(request) -> HttpResponse:
    books = Book.objects.all().order_by('title') # El unico llamado a la DB que hago
    number_books = books.count() # Esto se aplica sobre el object
    avg_rating = books.aggregate(Avg('rating'), Min('rating'), Max('rating'))
    
    return render(request, 'book_outlet/index.html', {
        'books': books,
        'number_books': number_books,
        'avg_rating': avg_rating
    })
    

def book_detail(request, slug) -> HttpResponse:
    # try: 
    #     book = Book.objects.get(pk=id) # pk: primary key
    # except:
    #     raise Http404()
    
    book = get_object_or_404(Book, slug=slug) # Es lo mismo que lo de arriba.
    return render(request, 'book_outlet/book_detail.html', {
        'title': book.title,
        'author': book.author,
        'rating': book.rating,
        'is_bestseller': book.is_best_selling
    })