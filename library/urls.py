from django.urls import path

from library import views

urlpatterns = [
    path('createbook/', views.create_book, name='createbook'),
    path('createAuthor/', views.create_author, name='createauthor'),
    path('getBook/<int:pk>', views.get_book_by_id, name = 'getbook'),
    path('getAuthor/<int:pk>', views.get_author_by_id, name = 'getbook')
]