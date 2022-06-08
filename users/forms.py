from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms

from users.models import Profile



# class CustomAuthForm(AuthenticationForm):
#     def __init__(self, *args, **kwargs):
#         super(CustomAuthForm, self).__init__(*args, **kwargs)
#         self.fields['username'].widget.attrs.update({'placeholder':'Username'})
#         self.fields['password'].widget.attrs.update({'placeholder':'Password'})


class UserRegisterForm(UserCreationForm):
    email = forms.CharField(label='Email')
    full_name = forms.CharField(max_length=50)

    def __init__(self, *args, **kwargs):
        '''
        This function helps add custom placeholders on the registration form
        '''
        super(UserRegisterForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'placeholder':'Username'})
        self.fields['email'].widget.attrs.update({'placeholder':'Email'})
        self.fields['full_name'].widget.attrs.update({'placeholder':'Full name'})
        self.fields['password1'].widget.attrs.update({'placeholder':'Password'})
        self.fields['password2'].widget.attrs.update({'placeholder':'Password confirmation'})
    #add widgets -placeholder
    # def __init__(self, *args, **kwargs):
    #     super(UserRegisterForm, self).__init__(*args, **kwargs)
    #     for field_name in self.fields:
    #         field = self.fields.get(field_name)  
    #         if field:
    #             if type(field.widget) in (forms.TextInput, forms.PasswordInput):
    #                 field.widget = forms.TextInput(attrs={'placeholder': field.label})

   


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