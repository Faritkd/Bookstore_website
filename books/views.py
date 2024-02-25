from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.db.models import Q
from django.views.generic import ListView, DetailView
from . import models
from .models import Book


# Create your views here.


class BookListView(LoginRequiredMixin, ListView):
    model = models.Book
    template_name = "books/book_list.html"
    login_url = "account_login"


class BookDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = models.Book
    template_name = "books/book_detail.html"
    login_url = "account_login"
    permission_required = "books.special_status"


class SearchResultsListView(ListView):
    model = models.Book
    template_name = "books/search_results.html"

    def get_queryset(self):
        query = self.request.GET.get("q")
        return Book.objects.filter(Q(title__icontains=query) | Q(author__icontains=query))

