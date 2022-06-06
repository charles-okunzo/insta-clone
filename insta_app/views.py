from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from insta_app.models import Post
from django.views.generic import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

# Create your views here.


def home(request):
    context={}
    return render(request,'insta_app/index.html', context)
    
@login_required
def posts(request):
    title  = 'Instagram | All posts'
    posts = Post.objects.order_by('-posted_date').all()
    context = {
        'title':title,
        'posts':posts
    }
    return render(request, 'insta_app/posts.html', context)


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['image_caption', 'image_name', 'image_path']
    success_url = '/posts'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['image_caption']
    success_url = '/posts'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.user:
            return True
        return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/posts'


    def test_func(self):
        post = self.get_object()
        if self.request.user == post.user:
            return True
        return False

