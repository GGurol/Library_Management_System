import django_filters
from .models import Book

class BookFilter(django_filters.FilterSet):
    is_available = django_filters.BooleanFilter(method='filter_by_availability')

    class Meta:
        model = Book
        fields = ['author', 'genres']

    def filter_by_availability(self, queryset, name, value):
        if value:
            return queryset.filter(copies__gt=0)
        else:
            return queryset.filter(copies=0)