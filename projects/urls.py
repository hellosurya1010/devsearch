from django.urls import path
from . import views

urlpatterns = [
    path('', views.projects, name="projects"),
    path('project/<str:id>/', views.project, name="project"),
    path('create', views.createProject, name="create-project"),
    path('update/<str:id>', views.updateProject, name="update-project"),
    path('delete/<str:id>', views.deleteProject, name="delete-project"),
]
