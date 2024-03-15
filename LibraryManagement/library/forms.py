from django import forms
from django.contrib.auth.forms import UserCreationForm
from library.models import User, Review
class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ["username" , "email" , "password1" , "password2"]

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ["rating" , "comment"]