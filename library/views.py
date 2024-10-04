from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from library.models import Book,Author
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

@api_view(['GET'])
def get_book_by_id(request):
    book_id = request.query_params.get('book_id')

    # If no book_id is provided, return bad request
    if not book_id:
        return Response({"error": "book_id is required"}, status=status.HTTP_400_BAD_REQUEST)

    book=get_object_or_404(Book,id=book_id)
    book_serializer = BookSerializer(book)

    return Response(book_serializer.data, status=status.HTTP_200_OK)

# TODO: GET AUTHOR BY ID and return json response..


@api_view(['GET'])
def get_author_by_id(request):
    author_id = request.query_params.get('author_id')

    # If no book_id is provided, return bad request
    if not author_id:
        return Response({"error": "author_id is required"}, status=status.HTTP_400_BAD_REQUEST)
    book = get_object_or_404(Author, id=author_id)
    author_serializer =AuthorSerializer(book)

    return Response(author_serializer.data, status=status.HTTP_200_OK)
