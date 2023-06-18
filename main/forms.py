from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import get_user_model

User = get_user_model()
class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'search', 'placeholder':'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'search', 'placeholder':'Password'}))

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'about', 'first_name', 'last_name']
        widgets = {
            'first_name': forms.TextInput(attrs={'class':'name-field', 'placeholder': 'Enter First Name'}),
            'last_name': forms.TextInput(attrs={'class':'name-field', 'placeholder': 'Enter Last Name'}),
            'username': forms.TextInput(attrs={'placeholder': 'Enter new username'}),
            'about': forms.Textarea(attrs={'placeholder': 'Tell us more about yourself', 'rows': '4'}),
        }