from django.urls import path

from apps.info.views import ContactUsView
from apps.info.views import AboutUsView

urlpatterns = [
    path('contact-us/', ContactUsView.as_view(), name='contact_us'),
    path('about-us/', AboutUsView.as_view(), name='about_us'),
]
