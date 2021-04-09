from django.shortcuts import render
from .models import Post
from django.views.generic import ListView, DetailView
# Create your views here.

class Index(ListView):
    model = Post
    template_name = 'index.html'


class Detail(DetailView):
    model = Post
    template_name='reading.html'

def newpost(req):
    if req.method == 'POST': 
        ...
    return render(req, 'newpost.html')