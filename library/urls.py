from django.urls import path

from library import views

urlpatterns = [
    path('createbook/', views.create_book, name='createbook'),
    path('createAuthor/', views.create_author, name='createauthor'),
    path('getBook/', views.get_book, name='getbook'),
    path('getAuthor/', views.get_author, name='getauthor'),
]