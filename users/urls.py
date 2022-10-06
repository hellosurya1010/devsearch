from sys import prefix
from django.urls import path
from . import views

prefix =  "users."

urlpatterns = [
    path('', views.index, name=prefix+"index"),
    path('show/<str:id>', views.show, name=prefix+"show"),
    path('login', views.loginUser, name="login"),
    path('logout', views.logoutUser, name="logout"),
    path('register', views.registerUser, name="register"),
]
