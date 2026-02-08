from django.urls import path

from . import views

urlpatterns = [
    path("", views.index),
    path("<slug:slug>", views.book_detail, name='book-detail') # digo id porque en la view function yo defini que recibiría id.
]

