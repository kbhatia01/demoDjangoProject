from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from library.serializer import BookSerializer
from library.serializer import AuthorSerializer
from library.models import Author, Book

# Create your views here.

@api_view(['POST'])
def create_book(request):
    book_serializer = BookSerializer(data = request.data)

    if book_serializer.is_valid():
        book_serializer.save()
        return Response(book_serializer.data, status = status.HTTP_201_CREATED)
    
@api_view(['POST'])
def create_author(request):
    author_serializer = AuthorSerializer(data = request.data)

    if author_serializer.is_valid():
        author_serializer.save()
        return Response(author_serializer.data, status = status.HTTP_201_CREATED)
    
@api_view(['GET'])
def get_author(request, id):
    try:
        author = Author.objects.get(pk=id)
    except Author.DoesNotExist:
        return Response({'error': 'Author Not Found'}, status = status.HTTP_404_NOT_FOUND)
    author_serialized = AuthorSerializer(author)
    return Response(author_serialized.data, status = status.HTTP_200_OK)


@api_view(['GET'])
def get_book(request, id):
    try:
        book = Book.objects.get(pk=id)
    except Book.DoesNotExist:
        return Response({'error': 'Book Not Found'}, status = status.HTTP_404_NOT_FOUND)
    book_serialized = BookSerializer(book)
    return Response(book_serialized.data, status = status.HTTP_200_OK)

