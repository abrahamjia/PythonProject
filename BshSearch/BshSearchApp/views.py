from django.shortcuts import render

# Create your views here.
from django.http import HttpRequest

def Index(request):

    return render(request,'Index.html')