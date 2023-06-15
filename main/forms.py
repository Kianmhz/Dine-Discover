from django import forms
from django.contrib.auth.forms import AuthenticationForm

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'search', 'placeholder':'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'search', 'placeholder':'Password'}))