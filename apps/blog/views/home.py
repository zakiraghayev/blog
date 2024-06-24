

from django.views.generic import ListView
from apps.blog.models import Article


class HomeView(ListView):
    model = Article
    template_name = 'blog/home.html'
    context_object_name = 'articles'
