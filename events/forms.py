from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Profile


class SignUpForm(UserCreationForm):
    username = forms.CharField(
        max_length=150,
        widget=forms.TextInput(attrs={
            'class': 'w-full rounded-md border-gray-300 px-4 py-2 shadow-sm focus:border-indigo-500 focus:ring-2 focus:ring-indigo-500 text-sm transition',
            'placeholder': 'Enter your username'
        })
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'class': 'w-full rounded-md border-gray-300 px-4 py-2 shadow-sm focus:border-indigo-500 focus:ring-2 focus:ring-indigo-500 text-sm transition',
            'placeholder': 'Enter your email'
        })
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'w-full rounded-md border-gray-300 px-4 py-2 shadow-sm focus:border-indigo-500 focus:ring-2 focus:ring-indigo-500 text-sm transition',
            'placeholder': 'Enter your password'
        })
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'w-full rounded-md border-gray-300 px-4 py-2 shadow-sm focus:border-indigo-500 focus:ring-2 focus:ring-indigo-500 text-sm transition',
            'placeholder': 'Confirm your password'
        })
    )

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        
        
class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['phone', 'location', 'bio'] 