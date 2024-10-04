from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from library.serializer import BookSerializer
from library.serializer import AuthorSerializer
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