from django.shortcuts import render
from .models import *


def home_page(request):
    data = Post.objects.all()
    return render(request, 'website/index.html', {'posts': data})


def single(request, id):
    data = Post.objects.get(id=id)
    return render(request, 'website/single.html', {'post': data})


def contato(request):
    return render(request, 'website/contact.html')


def save_form(request):
    name = request.POST['name']
    email = request.POST['email']
    message = request.POST['message']

    Contact.objects.create(
        name=name,
        email=email,
        message=message
    )
    return render(request, 'website/success_form.html', {'name': name, 'email': email, 'message': message})


def about(request):
    return render(request, 'website/about.html')
