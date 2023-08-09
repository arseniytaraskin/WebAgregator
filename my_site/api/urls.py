from django.urls import path
from rest_framework import routers
from .views import *
from django.views.generic import TemplateView

# router = routers.DefaultRouter()
# router.register('project', ProjectViewSet)
#
# urlpatterns = router.urls

urlpatterns = [
    path('', LeadProjectCreate.as_view())
]