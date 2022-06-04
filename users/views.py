from django.contrib import messages
from django.shortcuts import redirect, render
from .forms import UserRegisterForm

# Create your views here.


def register(request):
    form = UserRegisterForm()
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'An account for {username} has  been created successfully. You can now login')
            return redirect('home')
    return render(request, 'users/register.html', {'form':form})
