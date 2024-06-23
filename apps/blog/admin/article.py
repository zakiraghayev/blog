from django.contrib import admin

from apps.blog.models import Article
from apps.blog.models import Category

admin.site.register(Category)
admin.site.register(Article)
