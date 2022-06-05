from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms

from users.models import Profile



class UserRegisterForm(UserCreationForm):
    email = forms.CharField()
    full_name = forms.CharField(max_length=50)


    class Meta:
        model = User
        fields = ['email', 'full_name', 'username', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    email = forms.CharField()
    full_name = forms.CharField(max_length=50)



    class Meta:
        model = User
        fields = ['email', 'full_name', 'username']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['profile_pic', 'bio']