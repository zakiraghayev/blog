from django.contrib import admin

from apps.blog.models import Like
from apps.blog.models import Comment

admin.site.register(Like)
admin.site.register(Comment)
