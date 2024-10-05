from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def hello_world(request, name):
    return HttpResponse("Hello " + name)

def bye(request):
    return HttpResponse("Good Bye!")

def whatismyname(request):
    return HttpResponse("I dont know")
