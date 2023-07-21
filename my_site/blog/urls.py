from django.urls import path
from .views import (
    PostListView,
    UserPostListView
)

from .views import AddVideo, ViewVideo, VideoFile
from . import views

urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
    path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),
    #path('post/new/', NewVideo.as_view(), name='post-create'),
    path('new_video', AddVideo.as_view()),
    path('video/<int:id>/', ViewVideo.as_view()),
    path('get_video/<file_name>', VideoFile.as_view()),
    #path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('about/', views.about, name='blog-about'),
]