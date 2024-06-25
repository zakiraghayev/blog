from django.shortcuts import render, get_object_or_404
from django.views import View

from apps.info.models import AboutUs


class AboutUsView(View):
    def get(self, request):
        about_us = get_object_or_404(AboutUs)
        return render(request, 'info/about_us.html', {'page': about_us})
