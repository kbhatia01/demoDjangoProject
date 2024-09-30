from django.urls import path
from tryHello import views

urlpatterns = [path('hello/<str:name>', views.hello_world, name='hello'),
               path('bye/', views.bye, name='bye')]
