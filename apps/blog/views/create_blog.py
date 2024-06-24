from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from apps.blog.forms import ArticleForm

from apps.blog.models import Article


class ArticleCreateView(CreateView):
    model = Article
    form_class = ArticleForm
    template_name = 'blog/create-blog.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
