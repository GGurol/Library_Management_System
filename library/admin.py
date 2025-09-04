from django.contrib import admin
from django.contrib.auth.admin import UserAdmin 
from .models import User
from .models import Book
from .models import Borrow
from .models import Review
from .models import Genre


# Register your models here.
class MyUserAdmin(UserAdmin):
    add_fieldsets = (
    (
        None , 
        {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2', 'role')
        },
    ),
)

admin.site.register(User , MyUserAdmin)
admin.site.register(Book)
admin.site.register(Borrow)
admin.site.register(Review)
admin.site.register(Genre)