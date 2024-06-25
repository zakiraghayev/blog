from django.db import models
from ckeditor.fields import RichTextField


class AboutUs(models.Model):
    title = models.CharField(max_length=200, default="Haqqımızda")
    content = RichTextField()

    class Meta:
        verbose_name = "Haqqımızda"
        verbose_name_plural = "Haqqımızda"

    def __str__(self):
        return self.title
