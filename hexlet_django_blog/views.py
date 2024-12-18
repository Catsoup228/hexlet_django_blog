# hexlet_django_blog/views.py
from django.shortcuts import render
from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['who'] = 'World'
        return context

def about(request):
    return render(request, 'about.html')

def index(request):
    app_name = 'article'
    return render(request, 'articles/index.html', context = {'app_name':app_name})