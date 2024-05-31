from django.shortcuts import render, get_object_or_404
from .models import Author, Book
from books import views

def author_details(request, name):
    author = get_object_or_404(Author, name=name)
    return render(request, 'author_details.html', {'author': author})

def author_list(request):
    authors = Author.objects.all()
    return render(request, 'author_list.html', {'authors': authors})

def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, 'book_detail.html', {'book': book})

def book_list(request):
    books = Book.objects.all()
    return render(request, 'book_list.html', {'books': books})

def book_list_ordered(request):
    books = Book.objects.order_by('title')
    return render(request, 'book_list_ordered.html', {'books': books})
