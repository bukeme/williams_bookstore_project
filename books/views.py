from django.shortcuts import render
from django.db.models import Q
from books.models import Book
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

# Create your views here.

class BookListView(LoginRequiredMixin, generic.ListView):
    model = Book
    template_name = 'books/book_list.html'
    context_object_name = 'book_list'
    login_url = 'account_login'


class SearchResultListView(LoginRequiredMixin, generic.ListView):
    
    template_name = 'books/search_result.html'
    context_object_name = 'book_list'
    login_url = 'account_login'

    def get_queryset(self):
        query = self.request.GET['q']
        return Book.objects.filter(
            Q(title__icontains=query) |
            Q(author__icontains=query)
        )

class BookDetailView(LoginRequiredMixin, PermissionRequiredMixin, generic.DetailView):
    model = Book
    template_name = 'books/book_detail.html'
    login_url = 'account_login'
    permission_required = 'books.special_status'
