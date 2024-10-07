from django.urls import path
from library import views

urlpatterns = [
    path('createbook/', views.create_book, name='createbook'),
    path('createauthor/', views.create_author, name='createauthor'),
    path('getauthor/<int:id>', views.get_author, name='getauthor'),
    path('getbook/<int:id>', views.get_book, name='getbook')
]