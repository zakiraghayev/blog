from django.db import models


class ContactUs(models.Model):
    title = models.CharField(max_length=200, default="Əlaqə")
    content = models.TextField()

    class Meta:
        verbose_name = "Əlaqə"
        verbose_name_plural = "Əlaqə"

    def __str__(self):
        return self.title
