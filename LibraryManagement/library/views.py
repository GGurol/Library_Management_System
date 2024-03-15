from django.shortcuts import render
from django.db.models import Q
# Create your views here.

from django.shortcuts import render, redirect, get_object_or_404
from .forms import RegistrationForm, ReviewForm
from django.contrib.auth import login, logout, authenticate
from .models import *
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from datetime import datetime, timedelta
from .filters import BookFilter
# Create your views here.

def home_page(request):
    return render(request , 'home.html')

def sign_up(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/home')

    else:
        form = RegistrationForm()

    return render(request, 'registration/sign_up.html', {"form": form} )

def logout(request):
    logout(request)
    return redirect ('/home')

def all_books(request):
    allbooks = Book.objects.all()
    book_filter = BookFilter(request.GET , queryset = allbooks)
    if 'query' in request.GET:
        query = request.GET['query'] 
        multiple_query = Q(Q(title__icontains = query) | Q(author__contains = query))
        allbooks = Book.objects.filter(multiple_query)
    else:
        allbooks = book_filter.qs
    return render(request , 'allbooks.html' , {'allbooks' : allbooks , 'book_filter': book_filter})

def book_detail(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    reviews = Review.objects.filter(book=book)
    has_borrowed = Borrow.objects.filter(book=book, user=request.user).exists()
    has_reviewed =  Review.objects.filter(book=book , user=request.user ).exists()

    if request.method == 'POST' and has_borrowed:
        form = ReviewForm(request.POST)
        if form.is_valid():
            new_review = form.save(commit=False)
            new_review.book = book
            new_review.user = request.user
            new_review.save()
            messages.success(request, "Thank You for the Review! Review added successfully!")
            return redirect('book_detail', book_id = book_id)
    else:
        form = ReviewForm()
    return render(request, 'book_detail.html', {'book': book, 'reviews': reviews, 'form': form , 'has_borrowed': has_borrowed , 'has_reviewed': has_reviewed})

def borrow(request, user_id, book_id):
    if request.method == 'POST':
        user = get_object_or_404(User, pk=user_id)
        book = get_object_or_404(Book, pk=book_id)
        
        if Borrow.objects.filter(user=user, book=book , is_returned = False).exists():
            messages.error(request, "You have already borrowed this book.")
            return redirect('book_detail', book_id=book_id)
        
        num_borrowed_books = Borrow.objects.filter(user=user , is_returned = False).count()
        if num_borrowed_books >= 3:
            messages.error(request, "You have already borrowed the maximum number of books. Return th books to borrow another")
            return redirect('book_detail', book_id=book_id)

        borrow_date = datetime.now().date()
        return_date = borrow_date + timedelta(days=7)

        borrow = Borrow.objects.create(
            user=user,
            book=book,
            borrow_date=borrow_date,
            return_date=return_date
        )
        borrow.save()
        book.copies -= 1
        book.save()
        messages.success(request , "Borrowed book successfuly! ")

        return redirect('book_detail', book_id=book_id) 
    else:
        messages.error(request , "Some thing went wrong try again" )

@login_required
def borrowed_books(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    borrowings = Borrow.objects.filter(user=user, is_returned=False)
    books_with_dates = [(borrow.book, borrow.return_date, borrow) for borrow in borrowings]
    return render(request, 'borrowed_books.html', {'books_with_dates': books_with_dates})

def return_book(request, borrow_id):
    borrowed_book = get_object_or_404(Borrow, pk=borrow_id)
    borrowed_book.is_returned = True
    borrowed_book.save()
    returned_book = get_object_or_404 (Book, pk=borrowed_book.book_id)
    returned_book.copies += 1 
    returned_book.save()


    return redirect('borrowed_books', user_id=borrowed_book.user.pk)

