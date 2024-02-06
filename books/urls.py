from django.urls import path
from books import views

urlpatterns = [
    path('', views.BookListView.as_view(), name="book_list"),
    path('<slug:slug>/', views.BookDetailView.as_view(), name="book_detail"),
]