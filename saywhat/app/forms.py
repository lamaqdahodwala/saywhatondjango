from django.forms import ModelForm
from .models import Post
from django.contrib.auth import login, authenticate
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
class PostModelForm(ModelForm):
    class Meta:
        model=Post
        fields = ['title', 'author', 'body']

class CreateForm(UserCreationForm):
    firstname = forms.CharField()
    lastname = forms.CharField()

    class Meta:
        model = User
        fields = ['firstname', 'lastname', 'username', 'password1', 'password2']