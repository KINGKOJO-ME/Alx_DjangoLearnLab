from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL


class Notification(models.Model):

    recipient = models.ForeignKey(
        User,
        related_name='notifications',
        on_delete=models.CASCADE
    )

    actor = models.ForeignKey(
        User,
        related_name='actor_notifications',
        on_delete=models.CASCADE
    )

    verb = models.CharField(max_length=255)

    target = models.CharField(max_length=255, blank=True, null=True)

    timestamp = models.DateTimeField(auto_now_add=True)

    read = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.actor} {self.verb}"