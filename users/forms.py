from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms



class UserRegisterForm(UserCreationForm):
    email = forms.CharField()
    full_name = forms.CharField(max_length=50)


    class Meta:
        model = User
        fields = ['email', 'full_name', 'username', 'password1', 'password2']