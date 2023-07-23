from django import forms
from .models import Project

class NewVideoFormFile(forms.Form):
    title = forms.CharField(label='Название', max_length=100)
    description = forms.CharField(label='Описание', max_length=1000)
    file = forms.FileField(label='Видеофайл')

class NewProjectFormFile(forms.Form):
    title = forms.CharField(label='Название', max_length=100)
    description = forms.CharField(label='Описание', max_length=1000)
    image = forms.ImageField(label='Обложка')
    file = forms.FileField(label='Папка с игрой')

