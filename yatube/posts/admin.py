from django.contrib import admin
# Из модуля models импортируем модель Post
from .models import Post


admin.site.register(Post)

class AuthorAdmin(admin.ModelAdmin):
    date_hierarchy = 'pub_date'