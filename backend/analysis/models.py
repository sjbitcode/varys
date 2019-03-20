from django.contrib.postgres.fields import JSONField
from django.db import models

from .enums import SERVICE_NAMES
from content.models import Tweet


class AnalysisResponse(models.Model):
    service = models.CharField(
        max_length=3,
        choices=SERVICE_NAMES,
        verbose_name='Third party service name'
    )
    tweet = models.ForeignKey(
        Tweet,
        on_delete=models.CASCADE,
        related_name='analyses',
        verbose_name='Parent tweet'
    )
    data = JSONField(default=dict)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.service} - Tweet ID {self.tweet.id}'
