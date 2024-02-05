from django.shortcuts import render
from django.views.generic import ListView
from . import models
# Create your views here.


class BookList(ListView):
    model = models.Book
    template_name = "books/book_list.html"
