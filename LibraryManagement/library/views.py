from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, redirect
from .forms import RegistrationForm
from django.contrib.auth import login, logout, authenticate
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