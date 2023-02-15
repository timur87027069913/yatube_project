from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse('Главная страница')


# Страница со списком Сообщения
def group_posts(request):
    return HttpResponse('Сообщения')


# Страница с информацией об одном сорте мороженого;
# view-функция принимает параметр pk из path()

#def ice_cream_detail(request, pk):
#    return HttpResponse(f'Мороженое номер {pk}') 
