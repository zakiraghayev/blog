

from django.urls import path

from apps.blog.views import HomeView
from apps.blog.views import ArticleCreateView
from apps.blog.views import WeatherAPIView


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('article/new/', ArticleCreateView.as_view(), name='article-create'),
    path('api/weather/', WeatherAPIView.as_view(), name='weather_api'),

]
