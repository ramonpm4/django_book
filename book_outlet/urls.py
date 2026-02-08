from django.urls import path

from . import views

urlpatterns = [
    path("", views.index),
    path("<int:id>", views.book_detail) # digo id porque en la view function yo defini que recibiría id.
]

