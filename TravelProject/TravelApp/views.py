from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.
def demo(request):
    obj=Place.objects.all()
    ob1=Person.objects.all()
    return render(request,"index.html",{'result':obj,'Result1':ob1})



# def About(request):
#     return render(request,"About.html")

# def Contact(request):
#     return render(request,"Contact.html")

def NumAdd(request):
    return render(request,"NumAdd.html")
def Addition(request):
    x=int(request.GET['num1'])
    y=int(request.GET['num2'])
    res=x+y
    return render(request,"Result.html",{'result':res})