from django.contrib import messages
from django.shortcuts import redirect, render
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm

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


def profile(request):

    context = {
        
    }
    return render(request, 'users/profile.html', context)


def update(request):
    u_form = UserUpdateForm
    p_form = ProfileUpdateForm

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'users/update.html', context)