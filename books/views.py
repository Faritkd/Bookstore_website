from django.shortcuts import render
from django.views.generic import ListView, DetailView
from . import models
# Create your views here.


class BookListView(ListView):
    model = models.Book
    template_name = "books/book_list.html"


class BookDetailView(DetailView):
    model = models.Book
    template_name = "books/book_detail.html"
