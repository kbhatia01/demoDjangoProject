from django.urls import path

from library import views

urlpatterns = [
    path('createbook/', views.create_book, name='createbook'),
    path('createAuthor/', views.create_author, name='createauthor'),
    path('books/',views.get_books,name='books'),
    path('authors/',views.get_authors,name='authors'),
]