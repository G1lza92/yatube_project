from django.shortcuts import render
from django.http import HttpResponse


# Главная страница
def index(request):    
    return HttpResponse('Главная страница')

# Посты отфильтрованные по группам
def group_posts(request, slug):
    return HttpResponse('Посты отфильтрованные по группам')
