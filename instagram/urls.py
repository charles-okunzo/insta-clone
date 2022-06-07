"""instagram URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from insta_app.views import PostCreateView, PostUpdateView, PostDeleteView
from users import views as users_views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('insta_app.urls')),
    path('register', users_views.register, name='register'),
    path('profile/<str:username>', users_views.profile, name='profile'),
    path('update/', users_views.update, name='update'),
    path('login/', auth_views.LoginView.as_view(template_name = 'users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name = 'users/logout.html'), name='logout'),
    path('post/new/', PostCreateView.as_view(), name='create-post'),
    path('post/<int:pk>/update', PostUpdateView.as_view(), name='update-caption'),
    path('post/<int:pk>/delete', PostDeleteView.as_view(), name='delete-post')


]


if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


