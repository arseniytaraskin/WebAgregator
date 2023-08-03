from django.contrib import admin
from .models import ProjectModel



class ProjectAdmin(admin.AdminSite):
    list_display = ('title', 'description', 'image', 'file', 'views_count',
                    'user') #какие поля модели мы будем видеть в списке

    list_display_links = ('title') #по каким полям можем искать

    search_fields = ('title', 'description', 'image')

    list_editable = ('done', )
    list_filter = ('done', )


admin.site.register(ProjectModel)
