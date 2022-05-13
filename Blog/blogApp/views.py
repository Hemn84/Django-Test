from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
from .models import Post


def index(request):

    posts = Post.objects.all()
    print(posts is None)
    return render(request, "blogApp/index.html",{"posts":posts})
