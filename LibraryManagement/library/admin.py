from django.contrib import admin
from .models import User
from .models import Book
from .models import Borrow
from .models import Review
from .models import Genre


# Register your models here.

admin.site.register(User)
admin.site.register(Book)
admin.site.register(Borrow)
admin.site.register(Review)
admin.site.register(Genre)