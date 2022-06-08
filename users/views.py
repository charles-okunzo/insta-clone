from django.contrib import messages
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from insta_app.models import Post
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.models import User


# Create your views here.


def register(request):
    form = UserRegisterForm()
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'An account for {username} has  been created successfully. You can now login')
            return redirect('login')
    return render(request, 'users/register.html', {'form':form})

@login_required
def profile(request, username):
    posts = Post.objects.filter(user__username = request.user.username).all()
    # posts = Post.objects.order_by('-posted_date')
    if request.user.username != username:
        posts = Post.objects.filter(user__username = username).all()
        post_owner = User.objects.get(username = username)
        context = {
        'posts':posts,
        'post_owner': post_owner
        }
        return render(request, 'users/other_user_profile.html', context)

    context = {
        'posts':posts,
    }
    return render(request, 'users/profile.html', context)

@login_required
def update(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()

            messages.success(request, 'Your Profile has been updated successfully')
            return redirect('update')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
    
    context = {
        'u_form': u_form,
        'p_form': p_form,
    }

    return render(request, 'users/update.html', context)