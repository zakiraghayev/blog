

from django.urls import path

from apps.blog.views import HomeView


urlpatterns = [
    path('', HomeView.as_view(), name='home'),

]
