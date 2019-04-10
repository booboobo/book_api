from rest_framework import serializers

from .models import Book


class SnippetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('id', 'title', 'author', 'price', 'summary', 'publisher', 'image')
