from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, redirect, get_object_or_404
from .forms import RegistrationForm
from django.contrib.auth import login, logout, authenticate
from .models import Book
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
    return render(request , 'allbooks.html' , {'allbooks' : allbooks})

def book_detail(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    return render(request, 'book_detail.html', {'book': book})