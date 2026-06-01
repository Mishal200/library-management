from django.shortcuts import render, get_object_or_404, redirect
from .models import Book
from django.db.models import Q
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
def book_list(request):

    query = request.GET.get('q')

    books = Book.objects.all()

    if query:

        books = books.filter(
            Q(title__icontains=query) |
            Q(author__icontains=query) |
            Q(category__name__icontains=query)
        )

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


def issue_book(request, book_id):

    book = get_object_or_404(Book, id=book_id)

    if book.stock > 0:
        book.stock -= 1
        book.save()

    return redirect('book_detail', id=book.id)

def add_to_wishlist(request, book_id):

    wishlist = request.session.get('wishlist', [])

    if book_id not in wishlist:

        wishlist.append(book_id)

    request.session['wishlist'] = wishlist

    return redirect('wishlist')


def remove_from_wishlist(request, book_id):

    wishlist = request.session.get('wishlist', [])

    if book_id in wishlist:

        wishlist.remove(book_id)

    request.session['wishlist'] = wishlist

    return redirect('wishlist')



def categories(request):

    return render(request, 'books/categories.html')


def wishlist(request):

    wishlist_ids = request.session.get('wishlist', [])

    books = Book.objects.filter(id__in=wishlist_ids)

    return render(
        request,
        'books/wishlist.html',
        {'books': books}
    )

def profile(request):

    return render(request, 'books/profile.html')


def drama_books(request):

    books = Book.objects.filter(category__name='Drama')

    return render(
        request,
        'books/drama.html',
        {'books': books}
    )


def romance_books(request):

    books = Book.objects.filter(category__name='Romance')

    return render(
        request,
        'books/romance.html',
        {'books': books}
    )


def history_books(request):

    books = Book.objects.filter(category__name='History')

    return render(
        request,
        'books/history.html',
        {'books': books}
    )

def self_help_books(request):

    books = Book.objects.filter(category__name='Self-Help')

    return render(
        request,
        'books/self_help.html',
        {'books': books}
    )

def login_view(request):

    if request.method == 'POST':

        username = request.POST['username']

        password = request.POST['password']

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:
            login(request, user)
            return redirect('/')
    return render(request, 'books/login.html')