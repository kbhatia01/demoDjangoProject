from django.urls import path

from library import views

urlpatterns = [
    path('createbook/', views.create_book, name='createbook'),
    path('createAuthor/', views.create_author, name='createauthor'),
    path('book/<int:id>/', views.get_by_book_id, name='get_book_by_id'),
    path('author/<int:id>/', views.get_by_author_id, name='get_by_author_id'),
]