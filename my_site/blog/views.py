from django.shortcuts import render, get_object_or_404, HttpResponse, HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Video, Project
import os
from wsgiref.util import FileWrapper
from django.views.generic.base import View
from .forms import NewProjectFormFile
import random, string
from django.core.files.storage import FileSystemStorage

import zipfile

def upload_project(request):
    if request.method == 'POST':
        form = NewProjectFormFile(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/success/url/')
        else:
            form = NewProjectFormFile()
        return render(request, 'upload.html', {'form':form})


class ProjectFile(View):
    def get(self, request, file_name):

        BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

        file = FileWrapper(open(BASE_DIR+'/'+file_name, 'rb'))

        res = HttpResponse(file)

        res['Content-Disposition'] = f'attachment; filename={file_name}'

        return res



class ViewProject(View):
    def get(self, request, id):
        project_id = Project.objects.get(id=id)
        #project_id.path = 'http://localhost:8000/get_project/' + project_id.path



        file_zip = zipfile.ZipFile(project_id.file, 'r')
        #file_zip.extractall(f'./media/projects/{file_zip.filename}')
        file_zip.extractall(f'./blog/static/{file_zip.filename}')
        #print(file_zip.namelist())
        file_zip.close()

        # with zipfile.ZipFile(project_id.file, 'r') as file: #менеджер контекста
        #     # for item in file.infolist():
        #     #     print(f"File Name: {item.filename} Date: {item.date_time} Size: {item.file_size}")
        #
        #     file.extractall('./')

        context = {'project': project_id,
                   'project_path': file_zip.filename+'/index.html'}

        #print(project_id.file)
        return render(request, 'blog/project.html', context)
        #return render(request, f'./{project_id.file}/index.html', context)
        #return render(request, f'./media/projects/{file_zip.filename}/index.html')


class UnityWeb(View):
    def get(self, request, id):
        project_id = Project.objects.get(id=id)
        file_zip = zipfile.ZipFile(project_id.file, 'r')
        file_zip.close()
        content = { 'project':project_id,
                    'project_path':file_zip.filename,
                    'project_1':file_zip.filename+'/TemplateData/favicon.ico',
                    'project_2':file_zip.filename+'/TemplateData/style.css',
                    'project_3':file_zip.filename+'/TemplateData/UnityProgress.js',
                    'project_4':file_zip.filename+'/Build/UnityLoader.js',
                    'project_5':file_zip.filename+'/Build/pop it.json'}
        print(file_zip.filename)
        return render(request, 'blog/index.html', content)
        #return render(request, f'{file_zip.filename}/index.html')

class OpenProject(View):
    def get(self, request, id):
        project_id = Project.objects.get(id=id)
        file_zip = zipfile.ZipFile(project_id.file, 'r')
        file_zip.close()
        return render(request, f'{file_zip.filename}/index.html')

#представление для добавления проекта
class AddProject(View):
    def get(self, request):
        if request.user.is_authenticated == False:
            return HttpResponseRedirect('/')

        form = NewProjectFormFile()

        return render(request, 'blog/new_project.html', {'form': form})
    def post(self, request):
        form = NewProjectFormFile(request.POST, request.FILES)

        if form.is_valid():
            title = form.cleaned_data['title']

            description = form.cleaned_data['description']

            image = form.cleaned_data['image']

            file = form.cleaned_data['file']

            rnd = ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))

            path = rnd + file.name

            # preview_path = random_char + preview.name #

            file_s = FileSystemStorage(location=os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

            filename = file_s.save(path, file)
            # imagename = fs.save(preview_path, preview)

            new_project = Project(title=title, description=description, image=image, user=request.user, file=file, path=path)
            new_project.save()
            # return HttpResponse('Видео загружено')
            return HttpResponseRedirect(f'/project/{new_project.id}')
        else:
            return HttpResponse('Вы неправильно загрузили форму. Попробуйте еще раз.')

def home(request):
    #context = {
    #    'posts': Post.objects.all(),
    #    'videos': Video.objects.all()
    #}

    #return render(request, 'blog/home.html', context)

    def get(self, request):

        videos = Video.objects.order_by('-datetime')[:8]

        return render(request, 'blog/home.html', {'menu_active_item': 'home', 'most_recent_videos': videos})

#для отображения списка проектов на странице
class ProjectListView(ListView):
    model = Project
    template_name = 'blog/home.html' #путь к шаблону
    context_object_name = 'projects'
    ordering = ['-date_posted']
    paginate_by = 10

class PostListView(ListView):
    model = Project
    template_name = 'blog/home.html'
    context_object_name = 'projects'
    ordering = ['-date_posted']
    paginate_by = 5

class UserPostListView(ListView):
    model = Video
    template_name = 'blog/user_posts.html'
    context_object_name = 'videos'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Video.objects.filter(user=user).order_by('-date_posted')

def about(request):
    return render(request, 'blog/about.html', {'title': 'Все ролики автора: '})




