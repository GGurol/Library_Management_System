from django.urls import path
from . import views


urlpatterns = [
    path('',views.admindashboard, name='admindashboard'),
    path('admindashboard/',views.admindashboard, name='admindashboard'),
    path('manage-books/',views.manage_books, name='manage-books'),
    path('addbook/', views.add_book, name='add_book'),
    path('books/<int:book_id>/edit/', views.edit_book, name='edit_book'),
    path('books/<int:book_id>/delete/', views.delete_book, name='delete_book'),
    path('issued_books/', views.issued_books, name='issued_books'),
    path('student_list/', views.student_list, name='student_list'),
    path('ban_student/<int:student_id>', views.ban_student, name='ban_student'),
    path('unban_student/<int:student_id>', views.unban_student, name='unban_student'),
]

