from . import views
from django.urls import path, include

urlpatterns = [
    path('', views.home_page , name='home'),
    path('home/', views.home_page , name='home'),
    path('' , include('django.contrib.auth.urls')), 
    path('sign-up/', views.sign_up , name='sign_up'),
    path('logout/', views.logout, name='logout'),
    path ('all-books/' , views.all_books , name='all-books'),
    path('book/<int:book_id>/', views.book_detail, name='book_detail'),
]