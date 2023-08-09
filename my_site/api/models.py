from django.db import models
from users.forms import User
from django.core.validators import FileExtensionValidator

class ProjectModel(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    # image = models.ImageField(default='default.jpg', upload_to='projects_images/%Y-%m-%d/')
    # file = models.FileField(validators=[FileExtensionValidator(['zip'])])
    views_count = models.IntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


