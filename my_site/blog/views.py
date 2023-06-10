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
from .models import Post, Video
import os
from wsgiref.util import FileWrapper
from django.views.generic.base import View
from .forms import NewVideoForm
import random, string
from django.core.files.storage import FileSystemStorage

class VideoFileView(View):
    def get(self, request, file_name):
        BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        file = FileWrapper(open(BASE_DIR+'/'+file_name, 'rb'))
        response = HttpResponse(file, content_type='video/mp4')
        response['Content-Disposition'] = 'attachment; filename={}'.format(file_name)
        return response

class VideoView(View):
    template_name = 'blog/video.html' #страница с загрузкой

    def get(self, request, id):
        video_by_id = Video.objects.get(id=id)
        BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        video_by_id.path = 'http://localhost:8000/get_video/'+video_by_id.path
        context = {'video':video_by_id}

        return render(request, self.template_name, context) #вот здесь идет запрос на просмотр видео


class NewVideo(View):
    template_name = 'blog/new_video.html'

    def get(self, request):
        print(request.user.is_authenticated)
        if request.user.is_authenticated == False:
            # return HttpResponse('You have to be logged in, in order to upload a video.')
            return HttpResponseRedirect('/')

        form = NewVideoForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = NewVideoForm(request.POST, request.FILES)

        print(form)
        print(request.POST)
        print(request.FILES)

        if form.is_valid():
            title = form.cleaned_data['title']
            description = form.cleaned_data['description']
            file = form.cleaned_data['file']

            random_char = ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))
            path = random_char + file.name

            fs = FileSystemStorage(location=os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
            filename = fs.save(path, file)
            file_url = fs.url(filename)

            new_video = Video(title=title,
                              description=description,
                              user=request.user,
                              path=path)
            new_video.save()
            #return HttpResponse('Видео загружено')
            return HttpResponseRedirect('/video/{}'.format(new_video.id))
        else:
            return HttpResponse('You form is not valid. Go back and try again.')



def home(request):
    #context = {
    #    'posts': Post.objects.all()
    #}

    #return render(request, 'blog/home.html', context)
    template_name = 'blog/home.html'

    def get(self, request):
        most_recent_videos = Video.objects.order_by('-datetime')[:8]

        return render(request, self.template_name, {'menu_active_item': 'home',
                                                    'most_recent_videos': most_recent_videos})


class PostListView(ListView):
    model = Video
    template_name = 'blog/home.html'  
    context_object_name = 'videos'
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


class PostDetailView(DetailView):
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


def about(request):
    return render(request, 'blog/about.html', {'title': 'Все ролики автора: '})




