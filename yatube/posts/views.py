from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse('Ты <i>не можешь</i> получить правильные <b>ответы</b>,<br> '
        'если у тебя нет правильных <s>вопросов</s> запросов.')


# Страница со списком Сообщения
def group_posts(request):
    return HttpResponse('Сообщения')


# Страница с информацией об одном сорте мороженого;
# view-функция принимает параметр pk из path()

#def ice_cream_detail(request, pk):
#    return HttpResponse(f'Мороженое номер {pk}') 
