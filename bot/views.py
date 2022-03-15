import email
from email.headerregistry import Address
from functools import reduce
from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib.auth import logout,authenticate
from .models import user
from django.contrib import messages
from django import forms
from .forms import UsersForm
from django.http.response import HttpResponse
from django.http import HttpResponse
# Create your views here.
from django import *
import datetime
from django.conf import settings
from django.core.mail import send_mail


def home(request):
    # return HttpResponse("<h1>Hello World</h1>");
    username = request.session.get('username')
    if(username):
        context={}
        context["user1"] = user.objects.get(username = username)
        print(context["user1"].username)
        return render(request,'index.html',context)
    else:
        return render(request,'index.html')

def register(request):
    username = request.session.get('username')
    if(username):
        return redirect("/")
    return render(request, 'signup.html')

def registeruser(request):
    if(request.method == "POST"):
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        username = request.POST['username']
        password1 = request.POST['password']
        password2 = request.POST['confirm_password']
        email = request.POST['email']
        phone = request.POST['number']
        address = request.POST['address']
        reason = request.POST['reason']
        # current_datetime = datetime.datetime.now()
        
        
        if(password1 == password2):
            # user1 = user()
            if(user.objects.filter(username=username).exists()):
                messages.info(request, "Username is already taken !")
                return redirect('register')
            elif(user.objects.filter(email=email).exists()):
                messages.info(request,"Email is already taken")
                return redirect('register')
            else:
                # form = UsersForm(request.POST or None)
                # if form.is_valid():
                # 	form.save()
                # else:
                user1 = user(first_name=first_name,last_name=last_name,email=email,username=username,password=password1,phone=phone, Address=address, reason=reason)
                user1.save()
                subject = 'Welcome To PyGithub-Bots'
                message = f'Hi {first_name} {last_name}, Thank You For Registering In PyGithub-Bots\n\nHere, What we have received from you !\n\nFirst_name : {first_name}\nLast_name : {last_name}\nPhone : {phone}\nEmail : {email}\nUsername : {username}\nAddress : {address}\nPassword : {password1}\nReason : {reason}\n\nThanks & Regards\nPyGithub-Bot Team'
                email_from = settings.EMAIL_HOST_USER
                recipient_list = [email, ]
                send_mail( subject, message, email_from, recipient_list )
                request.session['username'] = username
                print("User Registered ", username)
        else:
            messages.info(request,"Both Password is not matching")
            return redirect('register')

        return redirect('/')

    else:
        return render(request,'signup.html')

def loginuser(request):
    if(request.method == "GET"):
        username = request.GET.get("username")
        password = request.GET.get("password")
        if(user.objects.filter(username=username).exists()):
            if(user.objects.filter(password=password).exists()):
                
                context = {}
                context["user1"] = user.objects.get(username = username)
                request.session['username'] = context['user1'].username
                # return redirect('/redirecttoindex')
                return HttpResponse('fine')
                # return render(request, 'index.html', context)
            else:
                return HttpResponse('Password Is Incorrect')
        else:
            return HttpResponse('Username Not Found')
    else:
        return HttpResponse('Not On Right Track')    
    

def userprofile(request, username):
    data = {}
    username1 = request.session.get('username')
    if(username and username1):
        data["userdata"] = user.objects.get(username = username)
        data["modul"] = data["userdata"].id % 13
        return render(request, "userprofile.html", data)
    else:
        return redirect("/")


def adminauth(request):
    if(request.method == "GET"):
        username = request.GET.get("username")
        password = request.GET.get("password")
        if(User.objects.filter(username=username).exists()):
            if(User.objects.filter(password=password).exists()):
                request.session['adminusername'] = username
                return HttpResponse('fine')
            else:
                return HttpResponse('Password Is Incorrect')
        # print(users.value)
        # return render(request,"admin.html",context)
        else:
            return HttpResponse('Username Doesn''t Exist')
    else:
        return HttpResponse('Not On Right Track')

def adminpageconfirm(request):
    username = request.session.get('adminusername')
    if(username):
        users = list(user.objects.all())
        usercount=len(users)
        recentusers = users[usercount-7:]
        context={}
        context["username"] = username
        context["usercount"] = usercount
        context["recentusers"] = recentusers
        context["users"] = users
        print("Total Users" ,context["usercount"])
        return render(request,"admin.html",context)
    else:
        return redirect("/")

def logoutuser(request):
    logout(request)
    return redirect("/")

def usersedit(request):
    if(request.method == "GET"):
        username = request.session.get('username')
        editfname = request.GET.get("editfname")
        editlname = request.GET.get("editlname")
        editaddress = request.GET.get("editaddress")
        editphone = request.GET.get("editphone")

        if(username and editaddress and editfname and editphone and editlname):
            if(user.objects.filter(username=username).exists()):
                obj1 = user.objects.get(username=username)
                obj1.first_name = editfname
                obj1.last_name = editlname
                obj1.Address = editaddress
                obj1.phone = editphone
                obj1.save()
                return HttpResponse('fine')
            else:
                return HttpResponse('Something Went Wrong !!')
        else:
            return HttpResponse('All Fields Are Required')

def forgotpassuser(request):
    if(request.method == "POST" ):
        usernameforgot = request.POST.get("usernameforgot")
        if(usernameforgot):
            if(user.objects.filter(username=usernameforgot).exists()):
                obj2 = user.objects.get(username=usernameforgot)
                if(obj2):
                    email = obj2.email
                    subject = 'Welcome To PyGithub-Bots'
                    message = f'Hi {obj2.first_name} {obj2.last_name}\n\nYour Password Is This : {obj2.password}\n\nThanks & Regards\nPyGithub-Bot Team'
                    email_from = settings.EMAIL_HOST_USER
                    recipient_list = [email, ]
                    send_mail( subject, message, email_from, recipient_list )
                    messages.info(request, "Email Sent ! Kindly Check Your Email For Password")
                    return redirect("forgotpassuser")
            else:
                messages.info(request, "Username Doesn't Exist")
                return redirect("forgotpassuser")
        else:
            messages.info(request, "Username Is Empty")
            return redirect("forgotpassuser")
    else:
        return render(request,'forgotuser.html')