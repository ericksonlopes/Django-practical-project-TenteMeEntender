from django.shortcuts import render
from .models import *


def home_page(request):
    data = Post.objects.all()
    return render(request, 'index.html', {'posts': data})


def single(request, id):
    data = Post.objects.get(id=id)
    return render(request, 'single.html', {'post': data})


def contato(request):
    return render(request, 'contact.html')


def save_form(request):
    name = request.POST['name']
    email = request.POST['email']
    message = request.POST['message']

    Contact.objects.create(
        name=name,
        email=email,
        message=message
    )
    return render(request, 'success_form.html', {'name': name, 'email': email, 'message': message})
