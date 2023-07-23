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
from .forms import NewVideoFormFile, NewProjectFormFile
import random, string
from django.core.files.storage import FileSystemStorage

def upload_project(request):
    if request.method == 'POST':
        form = NewProjectFormFile(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/success/url/')
        else:
            form = NewProjectFormFile()
        return render(request, 'upload.html', {'form':form})


class VideoFile(View):
    def get(self, request, file_name):

        BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

        file = FileWrapper(open(BASE_DIR+'/'+file_name, 'rb'))

        res = HttpResponse(file, content_type='video/mp4')

        res['Content-Disposition'] = f'attachment; filename={file_name}'

        return res

class ProjectFile(View):
    def get(self, request, file_name):

        BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

        file = FileWrapper(open(BASE_DIR+'/'+file_name, 'rb'))

        res = HttpResponse(file)

        res['Content-Disposition'] = f'attachment; filename={file_name}'

        return res

class ViewVideo(View):
    def get(self, request, id):
        video_id = Video.objects.get(id=id)

        video_id.path = 'http://localhost:8000/get_video/' + video_id.path

        context = {'video':video_id}

        return render(request, 'blog/video.html', context) #вот здесь идет запрос на просмотр видео

class ViewProject(View):
    def get(self, request, id):
        project_id = Project.objects.get(id=id)
        project_id.path = 'http://localhost:8000/get_project/' + project_id.path

        context = {'project':project_id}

        return render(request, 'blog/project.html', context)

# class AddVideo(View):
#     def get(self, request):
#
#         if request.user.is_authenticated == False:
#             return HttpResponseRedirect('/')
#
#         form = NewVideoFormFile()
#
#         return render(request, 'blog/new_video.html', {'form': form})
#
#     def post(self, request):
#         form = NewVideoFormFile(request.POST, request.FILES)
#
#         if form.is_valid():
#             title = form.cleaned_data['title']
#
#             description = form.cleaned_data['description']
#
#             file = form.cleaned_data['file']
#
#             rnd = ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))
#
#             path = rnd + file.name
#
#             #preview_path = random_char + preview.name #
#
#             file_s = FileSystemStorage(location=os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
#
#             filename = file_s.save(path, file)
#             #imagename = fs.save(preview_path, preview)
#
#             new_video = Video(title=title, description=description, user=request.user, path=path)
#             new_video.save()
#             #return HttpResponse('Видео загружено')
#             return HttpResponseRedirect(f'/video/{new_video.id}')
#         else:
#             return HttpResponse('Вы неправильно загрузили форму. Попробуйте еще раз.')

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

            #file_s = FileSystemStorage(location=os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

            new_project = Project(title=title, description=description, image=image ,user=request.user, path=path)
            new_project.save()

            return HttpResponseRedirect(f'/')
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


# class PostDetailView(DetailView):
#     model = Post


# class PostCreateView(LoginRequiredMixin, CreateView):
#     model = Post
#     fields = ['title', 'content']
#
#     def form_valid(self, form):
#         form.instance.author = self.request.user
#         return super().form_valid(form)


# class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
#     model = Post
#     fields = ['title', 'content']
#
#     def form_valid(self, form):
#         form.instance.author = self.request.user
#         return super().form_valid(form)
#
#     def test_func(self):
#         post = self.get_object()
#         if self.request.user == post.author:
#             return True
#         return False


# class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
#     model = Post
#     success_url = '/'
#
#     def test_func(self):
#         post = self.get_object()
#         if self.request.user == post.author:
#             return True
#         return False


def about(request):
    return render(request, 'blog/about.html', {'title': 'Все ролики автора: '})




