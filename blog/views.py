from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from .models import Post

# Create your views here.

def index(request):
    posts = Post.objects.all()
    return render(request, 'index.html', {'posts': posts})

def post(request):
    return HttpResponse("I'm a single post page.")