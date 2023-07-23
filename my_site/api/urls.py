from django.urls import path
from .views import *
app_name = 'api'

urlpatterns = [
    path('projects/', ListProjectsView.as_view(), name='project-list')
]