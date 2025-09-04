from django import forms
from django.contrib.auth.forms import UserCreationForm , AuthenticationForm
from library.models import User, Review



class LoginForm (AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))

    
class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ["username" , "email" , "password1" , "password2"]

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ["rating" , "comment"]