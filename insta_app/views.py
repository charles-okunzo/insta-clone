from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from insta_app.models import Post
from django.views.generic import CreateView

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


class PostCreateView(CreateView):
    model = Post
    fields = ['image_caption', 'image_name', 'image_path']
    success_url = '/posts'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)