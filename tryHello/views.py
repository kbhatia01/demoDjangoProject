import datetime

from django.http import HttpResponse
from django.shortcuts import render

from tryHello.models import Student


# Create your views here.
def hello_world(request,name):
    # s1 = Student(name=name,age=10,  dob=datetime.date.today())
    # s1.save() # save to db..

    # student = Student.objects.get(name=name)
    # student.age = 10
    # student.save()

    return HttpResponse("Hello your age is")
