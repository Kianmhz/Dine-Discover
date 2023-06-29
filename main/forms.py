from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import get_user_model
from .models import Media

User = get_user_model()
class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'search', 'placeholder':'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'search', 'placeholder':'Password'}))

class UserUpdateForm(forms.ModelForm):
    avatar = forms.ImageField(required=False)
    class Meta:
        model = User
        fields = ['username', 'about', 'first_name', 'last_name']
        widgets = {
            'first_name': forms.TextInput(attrs={'class':'name-field', 'placeholder': 'Enter First Name'}),
            'last_name': forms.TextInput(attrs={'class':'name-field', 'placeholder': 'Enter Last Name'}),
            'username': forms.TextInput(attrs={'placeholder': 'Enter new username'}),
            'about': forms.Textarea(attrs={'placeholder': 'Tell us more about yourself', 'rows': '4'}),
        }

class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={'class':'search', 'placeholder':'Username'}),
            'email': forms.EmailInput(attrs={'class':'search', 'placeholder':'Email'}),
            'first_name': forms.TextInput(attrs={'class':'name-field', 'placeholder':'First Name'}),
            'last_name': forms.TextInput(attrs={'class':'name-field', 'placeholder':'Last Name'}),
            'password1': forms.PasswordInput(attrs={'class':'search', 'placeholder':'Password'}),
            'password2': forms.PasswordInput(attrs={'class':'search', 'placeholder':'Confirm Password'}),
        }