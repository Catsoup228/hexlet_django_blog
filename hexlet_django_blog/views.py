# hexlet_django_blog/views.py
from django.shortcuts import render

def index(request):
    return render(request, 'index.html', context={
        'who': 'World',
    })

def about(request):
    return render(request, 'about.html')

def index(request):
    app_name = 'article'
    return render(request, 'articles/index.html', context = {'app_name':app_name})