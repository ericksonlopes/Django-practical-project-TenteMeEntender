from django.shortcuts import render
from .models import Post


def home_page(request):
    data = Post.objects.all()
    return render(request, 'index.html', {'posts': data})


