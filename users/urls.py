from sys import prefix
from django.urls import path
from . import views

prefix =  "users."

urlpatterns = [
    path('', views.index, name=prefix+"index"),
    path('show/<str:id>', views.show, name=prefix+"show"),
    path('login', views.login, name=prefix+"login"),
    path('register', views.register, name=prefix+"register"),
]
