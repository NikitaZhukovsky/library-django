from django.urls import path, re_path
from catalog.views import (index, AuthorListView, AuthorDetailView, BookListView, BookDetailView,
                           BookInstanceDetail, reserve_book, owned_books)

urlpatterns = [
    path('', index, name='index'),
    path('authors/', AuthorListView.as_view(), name='authors'),
    path('books/', BookListView.as_view(), name='books'),
    re_path(r'^authors/(?P<pk>\d+)/$', AuthorDetailView.as_view(), name='author-detail'),
    re_path(r'^books/(?P<pk>\d+)/$', BookDetailView.as_view(), name='book-detail'),
    re_path(r'^books_instance/(?P<pk>\d+)/$', BookInstanceDetail.as_view(), name='book_instance-detail'),
    path('reserve-book/<int:book_instance_id>/', reserve_book, name='reserve_book'),
    path('owned-books/', owned_books, name='owned_books'),
]

