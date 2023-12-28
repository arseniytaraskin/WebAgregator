from django.urls import path

from .views import *
from . import views

urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
    path('user/<str:username>', UserPostListView.as_view(), name='user-projects'),
    path('projects/', ProjectListView.as_view()),
    path('project/<int:id>', ViewProject.as_view()),
    path('new_project/', AddProject.as_view()),
    path('get_project/<file_name>', ProjectFile.as_view()),
    path('about/', views.about, name='blog-about'),
    path('unity/<int:id>', views.UnityWeb.as_view()),
    path('my_site/media/projects/projects/2023-07-25/pop_it_73IBn66.zip/<int:id>', views.OpenProject.as_view()),
    #path('api/get_project/', views.ProjectFileAPI.as_view())
]
