from . import views
from django.urls import path, include

urlpatterns = [
    path('', views.home_page , name='home'),
    path('home/', views.home_page , name='home'),
    path('' , include('django.contrib.auth.urls')), 
    path('sign-up/', views.sign_up , name='sign_up')
]