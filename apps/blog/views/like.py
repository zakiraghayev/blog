# blog/views.py

from django.shortcuts import get_object_or_404, redirect
from django.views import View
from django.contrib.auth.models import User

from apps.blog.models import Article
from apps.blog.models import Like


class LikeArticleView(View):
    def post(self, request, article_id):
        article = get_object_or_404(Article, id=article_id)
        ip_address = request.META.get('REMOTE_ADDR')

        if request.user.is_authenticated:
            user = request.user
            Like.objects.get_or_create(article=article, user=user)
        else:
            Like.objects.get_or_create(article=article, ip_address=ip_address)

        return redirect('home')
