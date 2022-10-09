from sys import prefix
from turtle import update
from django.urls import path
from . import views

prefix =  "users."

urlpatterns = [
    path('', views.index, name=prefix+"index"),
    path('show/<str:id>', views.show, name=prefix+"show"),
    path('account', views.account, name=prefix+"account"),
    path('account/edit', views.accountEdit, name=prefix+"account.edit"),
    path('login', views.loginUser, name="login"),
    path('logout', views.logoutUser, name="logout"),
    path('register', views.registerUser, name="register"),

    path('skill/', views.skill, name=prefix+'skill'),
    path('skill/update/<str:id>', views.skillUpdate, name=prefix+'skill.update'),
    path('skill/delete/<str:id>', views.skillDelete, name=prefix+'skill.delete'),

]
