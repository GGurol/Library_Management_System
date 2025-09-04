from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import BookForm
from django.contrib import messages
from library.models import *
from datetime import date, datetime
from django.db.models import Q
from django.db.models import Avg, Count
from .decorators import admin_required
from django.views.decorators.http import require_POST



@admin_required
def admindashboard(request):
    top_rated_books = Book.objects.annotate(avg_rating=Avg('review__rating')).order_by('-avg_rating')[:5]
    most_borrowed_books = Book.objects.annotate(num_borrows=Count('borrow')).order_by('-num_borrows')[:5]
    total_books = Book.objects.count()
    all_books = Book.objects.all()
    total_books = all_books.count()
    available_books = sum(book.is_available() for book in all_books)
    borrowed_books = Borrow.objects.filter(is_returned=False).count()
    today = date.today()
    overdue_books = Borrow.objects.filter(is_returned=False, return_date__lt=today).count()
    total_students = User.objects.filter(role='Student').count()
    return render(request, 'admindashboard.html', {
        'top_rated_books': top_rated_books,
        'most_borrowed_books': most_borrowed_books,
        'allbooks' : all_books,
        'total_books': total_books,
        'available_books': available_books,
        'borrowed_books': borrowed_books,
        'overdue_books': overdue_books, 
        'total_students': total_students
    })

@admin_required
def manage_books(request):
    if 'query' in request.GET:
        query = request.GET['query'] 
        multiple_query = Q(Q(title__icontains = query) | Q(author__contains = query))
        allbooks = Book.objects.filter(multiple_query)
    else:
        allbooks = Book.objects.all()
    return render(request , 'manage_books.html' , {'allbooks' : allbooks})

@admin_required
def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('manage-books') 
    else:
        form = BookForm()
    return render(request, 'add_book.html', {'form': form})

@admin_required
def edit_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('manage-books') 
    else:
        form = BookForm(instance=book)
    return render(request, 'edit_book.html', {'form': form})

@admin_required
def delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        book.delete()
        return redirect('manage-books')
    return render(request, 'delete_book.html', {'book': book})

from datetime import date

@admin_required    
def issued_books(request):
    issued_books = Borrow.objects.filter(is_returned=False).select_related('user', 'book')
    overdue_books = Borrow.objects.filter(is_returned=False, return_date__lt=date.today()).select_related('user', 'book')
    return render(request, 'issued_books.html', {'issued_books': issued_books, 'overdue_books': overdue_books})

from django.shortcuts import redirect

def student_list(request):
    query = request.GET.get('query')
    if query:
        students = User.objects.filter(
            role='Student',
            username__icontains=query
        ).annotate(
            num_borrowed_books=Count('borrow', filter=Q(borrow__is_returned=False)),
            num_returned_books=Count('borrow', filter=Q(borrow__is_returned=True)),
            num_pending_books=Count('borrow') - Count('borrow', filter=Q(borrow__is_returned=True))
        )
    else:
        students = User.objects.filter(role='Student').annotate(
            num_borrowed_books=Count('borrow', filter=Q(borrow__is_returned=False)),
            num_returned_books=Count('borrow', filter=Q(borrow__is_returned=True)),
            num_pending_books=Count('borrow') - Count('borrow', filter=Q(borrow__is_returned=True))
        )
    return render(request, 'student_list.html', {'students': students, 'query': query})

@require_POST
def ban_student(request, student_id):
    student = get_object_or_404(User, pk=student_id)
    if not student.is_banned:
        student.is_banned = True
        student.save()
        messages.success(request, f"{student.username} has been banned successfully.")
    return redirect('student_list')

@require_POST
def unban_student(request, student_id):
    student = get_object_or_404(User, pk=student_id)
    if student.is_banned:
        student.is_banned = False
        student.save()
        messages.success(request, f"{student.username} has been unbanned successfully.")
    return redirect('student_list')