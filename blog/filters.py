import django_filters
from .models import Publication, Category

class CategoryFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Category
        fields = ['name']

class PublicationFilter(django_filters.FilterSet):
    content = django_filters.CharFilter(lookup_expr='icontains')
    author = django_filters.NumberFilter(field_name='author__id')
    category = django_filters.NumberFilter(field_name='category__id')

    class Meta:
        model = Publication
        fields = ['content', 'author', 'category']
