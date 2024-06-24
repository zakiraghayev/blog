

from django.views.generic import ListView
from apps.blog.models import Article
from apps.blog.models import Like


class HomeView(ListView):
    model = Article
    template_name = 'blog/home.html'
    context_object_name = 'articles'

    def get_queryset(self):
        articles = super().get_queryset()
        ip_address = self.request.META.get('REMOTE_ADDR')
        for article in articles:
            if self.request.user.is_authenticated:
                article.user_has_liked = Like.objects.filter(
                    article=article, user=self.request.user).exists()
            else:
                article.user_has_liked = Like.objects.filter(
                    article=article, ip_address=ip_address).exists()
        return articles
