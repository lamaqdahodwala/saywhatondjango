from django.shortcuts import render
from .models import Post
from django.views.generic import ListView, DetailView, UpdateView, CreateView
from .forms import PostModelForm
# Create your views here.

class Index(ListView):
    model = Post
    template_name = 'index.html'


class Detail(DetailView):
    model = Post
    template_name='reading.html'

class NewPost(CreateView):
    model = Post
    template_name='newpost.html'