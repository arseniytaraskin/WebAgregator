from django.urls import path

from .views import *
from . import views

urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
    path('user/<str:username>', UserPostListView.as_view(), name='user-projects'),
    path('project/<int:id>', ViewProject.as_view()),
    path('new_project/', AddProject.as_view()),
    path('get_project/<file_name>', ProjectFile.as_view()),
    path('about/', views.about, name='blog-about'),
    path('unity/<int:id>', views.UnityWeb.as_view()),
    path('my_site/media/projects/projects/2023-07-25/pop_it_73IBn66.zip/<int:id>', views.OpenProject.as_view())

    #path('post/new/', NewVideo.as_view(), name='post-create'),
    #path('new_video', AddVideo.as_view()),
    #path('video/<int:id>/', ViewVideo.as_view()),
    #path('get_video/<file_name>', VideoFile.as_view()),
    #path('post/new/', PostCreateView.as_view(), name='post-create'),
]