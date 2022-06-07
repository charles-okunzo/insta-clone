from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name= 'home'),
    path('posts/', views.posts, name= 'posts'),
    path('search/', views.search_by_name, name='search'),
    path('likes/<int:pk>', views.postLike, name='post_like')
]