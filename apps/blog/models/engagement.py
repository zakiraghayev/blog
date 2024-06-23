from django.db import models
from django.contrib.auth.models import User

from apps.blog.models import Article
from commons.models import DateTimeModel


class Comment(DateTimeModel, models.Model):
    article = models.ForeignKey(
        Article,
        related_name='comments',
        on_delete=models.CASCADE
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )
    content = models.TextField()

    class Meta:
        verbose_name = "Rəy"
        verbose_name_plural = "Rəylər"

    def __str__(self):
        return f'Comment by {self.user} on {self.article}'


class Like(DateTimeModel, models.Model):
    article = models.ForeignKey(
        Article,
        related_name='likes',
        on_delete=models.CASCADE
    )
    user = models.ForeignKey(
        User,
        null=True,
        blank=True,
        on_delete=models.CASCADE
    )
    ip_address = models.GenericIPAddressField(null=True, blank=True)

    class Meta:
        verbose_name = "Bəyənmə"
        verbose_name_plural = "Bəyənmələr"

    def __str__(self):
        return f'Like by {self.user if self.user else self.ip_address} on {self.article}'
