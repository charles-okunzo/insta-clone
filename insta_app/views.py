from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from insta_app.forms import PostCommentForm
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
    comment_form = PostCommentForm()
    if request.method == 'POST':
        comment_form = PostCommentForm(request.POST)
        if comment_form.is_valid():
            comment_form.save()

        return redirect('posts')
    context = {
        'title':title,
        'posts':posts,
        'comment_form':comment_form
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
    success_url = '/profile'

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
    success_url = '/profile'


    def test_func(self):
        post = self.get_object()
        if self.request.user == post.user:
            return True
        return False

def search_by_name(request):
    if 'search_username' in request.GET and request.GET['search_username']:
        search_term = request.GET.get('search_username')
        searched_accounts  = Post.search_by_name(search_term)
        message = f'{search_term}'
        context = {
            'searched_accounts': searched_accounts,
            'message':message
        }
        return render(request, 'insta_app/search_accounts.html', context)
    else:
        message  = 'You have not searched any items'
        return render(request, 'insta_app/search_accounts.html', {'message':message})
