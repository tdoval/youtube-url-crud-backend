import uuid
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import URLValidator
from urls.domain.validators import validate_youtube_url
from django.utils import timezone

class VideoURLManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(deleted_at__isnull=True)

class VideoURL(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    url = models.URLField(max_length=255, validators=[URLValidator(), validate_youtube_url])
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    added_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    objects = VideoURLManager()

    def soft_delete(self):
        self.deleted_at = timezone.now()
        self.save()

    @property
    def is_deleted(self):
        return self.deleted_at is not None

    def __str__(self):
        return self.url
