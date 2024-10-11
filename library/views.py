from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from library.models import Book, Author
from library.serializer import BookSerializer, AuthorSerializer


# Create your views here.

@api_view(['POST'])
def create_book(request):
    book_serializer = BookSerializer(data=request.data)

    if book_serializer.is_valid():
        book_serializer.save()
        return Response(book_serializer.data, status=status.HTTP_201_CREATED)

    return Response(book_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def create_author(request):
    author_serializer = AuthorSerializer(data=request.data)

    if author_serializer.is_valid():
        author_serializer.save()

        return Response(author_serializer.data, status=status.HTTP_201_CREATED)

    return Response(author_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# TODO: GET BOOK BY ID and return json response..
# TODO: GET AUTHOR BY ID and return json response..


@api_view(['GET'])
def get_by_book_id(request, id):
    try:
        book = Book.objects.get(id=id)
    except Book.DoesNotExist:
        # If the book isn't found, return a 404 response
        return Response({"error": "Book not found"}, status=status.HTTP_404_NOT_FOUND)

    book_serializer = BookSerializer(book)
    return Response(book_serializer.data,  status = status.HTTP_200_OK)


@api_view(['GET'])
def get_by_author_id(request, id):
    try:
        author = Author.objects.get(id=id)
    except Author.DoesNotExist:
        return Response({"error": "Author not found"}, status=status.HTTP_404_NOT_FOUND)

    author_serializer = AuthorSerializer(author)
    return Response(author_serializer.data, status= status.HTTP_200_OK)




