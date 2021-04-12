from django.shortcuts import render, redirect
from django.core.handlers.wsgi import WSGIRequest
from .models import Post
from django import http
from django.views.generic import ListView, DetailView, UpdateView, CreateView
from .forms import PostModelForm, CreateForm
# Create your views here.

class Index(ListView):
    model = Post
    template_name = 'index.html'

class Detail(DetailView):
    model = Post
    template_name='reading.html'

def newpost(req:WSGIRequest):
    if req.method == "POST":
        form = PostModelForm(req.POST or None)
        print(form.is_valid())
        print(form.has_error('title'))
        print(form.has_error('author'))
        print(form.has_error('body'))
        if form.is_valid():
            form.save()
            print('saved')
            return redirect('index')
        else:
            print('not saved')
            return redirect('index')
    else:
        user = req.user 
        return render(req, 'newpost.html', {'user': user})

def register(req:WSGIRequest):
    if req.method == 'POST':
        form = CreateForm(req.POST or None)
        if form.is_valid():
            form.save()
            print('saved form')
            return redirect('/')
        else:
            print('not saved')
    form = CreateForm()
    return render(req, 'register.html', {'form': form})
