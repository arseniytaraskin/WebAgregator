from django import forms

class NewVideoFormFile(forms.Form):
    title = forms.CharField(label='Название', max_length=100)
    description = forms.CharField(label='Описание', max_length=1000)
    file = forms.FileField(label='Видеофайл')