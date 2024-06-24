# blog/views.py

from django.shortcuts import get_object_or_404, redirect, render
from django.views import View


from apps.blog.models import Article

from apps.blog.forms import CommentForm


class ArticleDetailView(View):
    def get(self, request, article_id):
        article = get_object_or_404(Article, id=article_id)
        comments = article.comments.all()
        comment_form = CommentForm()
        context = {
            'article': article,
            'comments': comments,
            'comment_form': comment_form,
        }
        return render(request, 'blog/detail-blog.html', context)

    def post(self, request, article_id):
        article = get_object_or_404(Article, id=article_id)
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.article = article
            comment.user = request.user
            comment.save()
            return redirect('article_detail', article_id=article.id)
        comments = article.comments.all()
        context = {
            'article': article,
            'comments': comments,
            'comment_form': comment_form,
        }
        return render(request, 'blog/detail-blog.html', context)
