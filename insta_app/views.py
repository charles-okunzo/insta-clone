
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.urls import reverse, reverse_lazy
from insta_app.forms import PostCommentForm
from insta_app.models import Comment, Post
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
            comment_form = PostCommentForm(request.POST)
            content = request.POST.get('comment')
            user = request.user.id
            post_id = request.POST.get('post-id')
            comment_ins = Comment(content = content, post = post_id, user = user)
            comment_ins.save()
            return redirect('posts')
        print(request.POST)
        print(request.user.id)
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
    success_url = '/profile/user'

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
    


    def test_func(self):
        post = self.get_object()
        if self.request.user == post.user:
            return True
        return False
    
    #after the deleting redirect to this url and pass in the arguments
    def get_success_url(self, **kwargs):
        if  kwargs != None:
            return reverse_lazy('profile', kwargs = {'username': self.request.user.username})
        

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

def postLike(request, pk):
    post_id = request.POST.get('post-id')
    post = Post.objects.get(pk=post_id)
    user = request.user

    if post.likes.filter(id=user.id).exists():
        post.likes.remove(user)
    else:
        post.likes.add(user)

    return HttpResponseRedirect(reverse('posts'))



