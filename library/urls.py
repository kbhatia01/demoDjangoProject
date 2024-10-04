from django.urls import path

urlpatters = [
    path('createbook/', views.create_book, name='createbook')
    path('createauthor/', views.create_author, name='createauthor')
]