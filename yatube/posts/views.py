from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    template = 'index.html'
    return render(request, template)


def group_posts(request):
    return HttpResponse('Сообщения')
