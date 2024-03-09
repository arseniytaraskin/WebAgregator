from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

import users.views
from users import views as user_views

from .yasg import urlpatterns as doc_url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/admin/', admin.site.urls), #
    path('register/', user_views.register, name='register'),
    path('api/register/', user_views.register, name='register'), #
    path('profile/', user_views.profile, name='profile'),
    path('api/profile/', user_views.GetProfile.as_view()), #
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('api/login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'), #
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('api/logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'), #
    path('', include('blog.urls')),
    path('api/', include('api.urls')),
    path('api/profile', users.views.UsersAPI.as_view())
    #path('api/', include('frontend.urls'))
    #path('project/', )
]

urlpatterns += doc_url

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
