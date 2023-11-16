from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User

class SignupForm(UserCreationForm):
    class Meta:
        model=User
        fields=('username','email','password1','password2')
    username=forms.CharField(widget=forms.TextInput(attrs={
        'placeholder':"your_name",
        'class':"rounded bg-gray-300 w-full py-1 px-3 !outline-none"
        }))
    email=forms.CharField(widget=forms.EmailInput(attrs={
        'placeholder':"add_your_email",
        'class':"rounded bg-gray-300 w-full py-1 px-3 !outline-none"
        }))
    password1=forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': "your_password",
        'class':"rounded bg-gray-300 w-full py-1 px-3 !outline-none"
        }))
    
    password2=forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': "confirm_your_password",
        'class':"rounded bg-gray-300 w-full py-1 px-3 !outline-none"
        }))
        
        # widgets = {
        #     'username': forms.TextInput(attrs={
        #         'placeholder': "your_name",
        #         'class': "rounded bg-gray-100 w-full py-1 px-3 !outline-none"
        #     }),
        #     'email': forms.EmailInput(attrs={
        #         'placeholder': "add_your_email",
        #         'class': "rounded bg-gray-100 w-full py-1 px-3 !outline-none"
        #     }),
        #     'password1': forms.PasswordInput(attrs={
        #         'placeholder': "your_password",
        #         'class': "rounded bg-gray-100 w-full py-1 px-3 !outline-none"
        #     }),
        #     'password2': forms.PasswordInput(attrs={
        #         'placeholder': "confirm_your_password",
        #         'class': "rounded bg-gray-100 w-full py-1 px-3 !outline-none"
        #     })
        # }
class LoginForm(AuthenticationForm):
    username=forms.CharField(widget=forms.TextInput(attrs={
        'placeholder':"your_name",
        'class':"rounded bg-gray-300 w-full py-1 px-3 !outline-none"
        }))
    password=forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': "your_password",
        'class':"rounded bg-gray-300 w-full py-1 px-3 !outline-none"
        }))
        