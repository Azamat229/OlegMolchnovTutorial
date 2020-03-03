from django.shortcuts import render
from . models import Post


def post_list(request):
    post = Post.objects.all()
    return render(request, "driver/index.html", context={'posts': post})
