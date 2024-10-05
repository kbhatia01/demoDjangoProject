from django.urls import path
from library import views

urlpatterns = [
    path('createbook/', views.create_book, name='createbook'),
    path('createauthor/', views.create_author, name='createauthor'),
]