from django.shortcuts import render, get_object_or_404
from .models import Book


def book_list(request):

    query = request.GET.get('q')

    books = Book.objects.all()

    if query:
        books = books.filter(title__icontains=query)

    return render(
        request,
        'books/book_list.html',
        {'books': books}
    )


def book_detail(request, id):

    book = get_object_or_404(Book, id=id)

    return render(
        request,
        'books/book_detail.html',
        {'book': book}
    )