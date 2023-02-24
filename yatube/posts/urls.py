from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:group_id>/', views.group_posts, name='group_list'),
]
