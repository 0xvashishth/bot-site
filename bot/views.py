import email
from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from .models import user
from django.contrib import messages
from django import forms
from .forms import UsersForm
from django.http.response import HttpResponse
from django.http import HttpResponse
# Create your views here.
from django import *
import datetime


def home(request):
	# return HttpResponse("<h1>Hello World</h1>");
	return render(request,'index.html')

def register(request):

    return render(request, 'signup.html')

def registeruser(request):
	if(request.method == "POST"):
		first_name = request.POST["first_name"]
		last_name = request.POST["last_name"]
		username = request.POST['username']
		password1 = request.POST['password']
		password2 = request.POST['confirm_password']
		email = request.POST['email']
		current_datetime = datetime.datetime.now()

		if(password1 == password2):
			if(User.objects.filter(username=username).exists()):
				messages.info(request, "Username is already taken !")
				return redirect('register')
			elif(User.objects.filter(email=email).exists()):
				messages.info(request,"Email is already taken")
				return redirect('register')
			else:
				# form = UsersForm(request.POST or None)
				# if form.is_valid():
				# 	form.save()
				# else:
				user1 = User.objects.create_user(first_name=first_name,last_name=last_name,email=email,username=username,password=password1,date_joined=current_datetime)
				user1.save()
				print("User Registered")
		else:
			messages.info(request,"Password is not matching")
			return redirect('register')

		return redirect('/')

	else:
		return render(request,'signup.html')

def loginuser(request):

	return render(request, 'index.html')