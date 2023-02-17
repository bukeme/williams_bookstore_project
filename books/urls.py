from django.urls import path
from books.views import BookListView, BookDetailView, SearchResultListView


urlpatterns = [
    path('', BookListView.as_view(), name='book_list'),
    path('search/', SearchResultListView.as_view(), name='search_results'),
    path('<uuid:pk>/', BookDetailView.as_view(), name='book_detail'),
]