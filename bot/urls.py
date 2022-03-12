from unicodedata import name
from django.urls import path
from django.urls.resolvers import URLPattern
from . import views

urlpatterns = [
	path('',views.home,name='home'),
    path('register', views.register, name="register"),
    path('login/', views.loginuser, name="loginuser"),
    path('registeruser/', views.registeruser, name="registeruser"),
    path("userprofile/<username>", views.userprofile, name="viewprofile"),
    path('logoutuser/', views.logoutuser, name="logout"),
    path('useredit/', views.usersedit, name="useredit"),
] 
