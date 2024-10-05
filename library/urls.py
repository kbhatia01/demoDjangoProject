from django.urls import path

from library import views

urlpatterns = [
    path('createBook/', views.create_book, name='createbook'),
    path('createAuthor/', views.create_author, name='createauthor'),
    path('book/<int:id>/', views.get_book_by_id, name='getBookByID'),
    path('author/<int:id>/', views.get_author_by_id, name='getAuthorByID'),
]