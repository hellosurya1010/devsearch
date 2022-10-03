from sys import prefix
from django.urls import path
from . import views

prefix =  "users."

urlpatterns = [
    path('', views.index, name=prefix+"index"),
    path('show/<str:id>', views.index, name=prefix+"show"),
]
