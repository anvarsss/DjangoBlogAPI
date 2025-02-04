from rest_framework import serializers
from .models import Publication, Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']

class PublicationSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    category = CategorySerializer(read_only=True)

    class Meta:
        model = Publication
        fields = ['id', 'title', 'content', 'author', 'category', 'created_at']
