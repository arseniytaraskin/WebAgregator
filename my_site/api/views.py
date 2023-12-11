from rest_framework.decorators import api_view
from rest_framework import generics

from my_site import settings
from .models import ProjectModel, MainPage
from .serializers import ProjectSerializer, MainPageSerializer
from django.http import HttpResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
import os
from wsgiref.util import FileWrapper

class LeadProjectCreate(generics.ListCreateAPIView):
    queryset = ProjectModel.objects.all()
    serializer_class = ProjectSerializer

class WebHtmlDocumentView(View):
    def get(self, request, file_name):
        BASE_DIR  = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        file = FileWrapper(open(BASE_DIR+'/'+file_name, 'rb'))

        if os.path.exists(BASE_DIR):
            result = HttpResponse(file, content_type='text/html')
            result['Content-Disposition'] = f'inline; filename="{file_name}"'
            return result
        else:
            return HttpResponse("HTML документ не найден", status=404)
class MainPageListCreateView(generics.ListCreateAPIView):
    queryset = MainPage.objects.all()
    serializer_class = MainPageSerializer

class HTMLDocumentView(View):
    @csrf_exempt
    def get(self, request, doc_name):
        # Путь к HTML-документу в папке project_docs
        doc_path = os.path.join(settings.BASE_DIR, 'project_docs', doc_name)

        # Проверяем, существует ли файл
        if os.path.exists(doc_path):
            with open(doc_path, 'rb') as doc_file:
                response = HttpResponse(doc_file.read(), content_type='text/html')
                response['Content-Disposition'] = f'inline; filename="{doc_name}"'
                return response
        else:
            return HttpResponse("HTML документ не найден", status=404)


# новые
class MainPageDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MainPage.objects.all()
    serializer_class = MainPageSerializer
