from django.shortcuts import render
from django.http.response import HttpResponse
from django.http import HttpResponse
# Create your views here.
from django import *

def home(request):
	# return HttpResponse("<h1>Hello World</h1>");
	return render(request,'index.html')

def register(request):
    return render(request, 'signup.html')

def loginuser(request):

	return render(request, 'index.html')