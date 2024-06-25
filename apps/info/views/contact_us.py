from django.shortcuts import render, get_object_or_404
from django.views import View

from apps.info.models import ContactUs


class ContactUsView(View):
    def get(self, request):
        contact_us = get_object_or_404(ContactUs)
        return render(request, 'info/contact_us.html', {'page': contact_us})
