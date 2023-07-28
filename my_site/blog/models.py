from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class Video(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    path = models.CharField(max_length=100)
    #image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    #preview = models.CharField(max_length=100)
    date_posted = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Project(models.Model):
    title = models.CharField(max_length=200) #название проекта
    description = models.TextField() #описание проекта
    #rools = models.TextField() #правила игры
    image = models.ImageField(default='default.jpg', upload_to='projects_images/%Y-%m-%d/') #главное изображение проекта
    file = models.FileField(upload_to='projects/%Y-%m-%d/')
    path = models.CharField(max_length=100)
    rating = models.IntegerField(default=0) #рейтинг проекта
    views = models.IntegerField(default=0) #кол-во просмотров проекта
    date_posted = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title