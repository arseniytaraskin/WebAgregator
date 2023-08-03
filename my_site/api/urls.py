from django.urls import path
from rest_framework import routers
from .api import *

app_name = 'api'

router = routers.DefaultRouter()
router.register('project', ProjectViewSet)

urlpatterns = router.urls