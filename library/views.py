from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Book,Author
from library.serializer import BookSerializer, AuthorSerializer
from rest_framework.exceptions import NotFound


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
def get_book_by_id(request,id):
    try:
        instance = Book.objects.get(pk=id)
    except Book.DoesNotExist:
        raise NotFound(f"No record found with ID {id}")

    serializer = BookSerializer(instance)
    return Response(serializer.data, status=status.HTTP_200_OK)


# TODO: GET AUTHOR BY ID and return json response..
@api_view(['GET'])
def get_author_by_id(request,id):
    try:
        instance = Author.objects.get(pk=id)
    except Author.DoesNotExist:
        raise NotFound(f"No record found with ID {id}")

    serializer = AuthorSerializer(instance)
    return Response(serializer.data, status=status.HTTP_200_OK)