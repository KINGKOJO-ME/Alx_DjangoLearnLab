from rest_framework import serializers
from .models import Author, Book
from datetime import datetime


# -------------------------------------------------------
# Book Serializer
# -------------------------------------------------------
# This serializer converts Book model instances into JSON
# and vice versa.
#
# It includes validation to ensure the publication year
# is not set in the future.
# -------------------------------------------------------

class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = '__all__'

    def validate_publication_year(self, value):
        """
        Custom validation to ensure the publication year
        is not in the future.
        """
        current_year = datetime.now().year

        if value > current_year:
            raise serializers.ValidationError(
                "Publication year cannot be in the future."
            )

        return value


# -------------------------------------------------------
# Author Serializer
# -------------------------------------------------------
# This serializer represents the Author model.
#
# It includes a nested BookSerializer to display
# all books written by the author.
#
# Relationship Handling:
# Author -> Books
# The related_name='books' in the Book model allows
# the serializer to dynamically retrieve all books
# associated with an author.
# -------------------------------------------------------

class AuthorSerializer(serializers.ModelSerializer):

    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['id', 'name', 'books']