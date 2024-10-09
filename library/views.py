from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from library.models import Author, Book
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
#127.0.0.1:8000/api/getBook?id=1
@api_view(['GET'])
def get_book(request):
    index = request.query_params.get('id')
    book_serializer = BookSerializer(Book.objects.get(pk=index))
    return Response(book_serializer.data, status=status.HTTP_200_OK)

#127.0.0.1:8000/api/getAuthor?id=1
# TODO: GET AUTHOR BY ID and return json response..
@api_view(['GET'])
def get_author(request):
    index = request.query_params.get('id')
    author_serializer = AuthorSerializer(Author.objects.get(pk=index))
    return Response(author_serializer.data, status=status.HTTP_200_OK)