from django.db import models
from django.contrib.auth.models import User

from commons.models import DateTimeModel


class Category(DateTimeModel, models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    class Meta:
        verbose_name = "Kateqoriya"
        verbose_name_plural = "Kateqoriyalar"

    def __str__(self):
        return self.name


class Article(DateTimeModel, models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    categories = models.ManyToManyField(
        Category,
        blank=True,
        related_name='articles'
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="articles"
    )

    class Meta:
        verbose_name = "Bloq"
        verbose_name_plural = "Bloqlar"

    def __str__(self):
        return self.title
