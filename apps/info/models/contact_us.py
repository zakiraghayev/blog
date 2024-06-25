from django.db import models
from ckeditor.fields import RichTextField


class ContactUs(models.Model):
    title = models.CharField(max_length=200, default="Əlaqə")
    content = RichTextField()

    class Meta:
        verbose_name = "Əlaqə"
        verbose_name_plural = "Əlaqə"

    def __str__(self):
        return self.title
