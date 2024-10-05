from django.db import models
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError
import re

def validate_youtube_url(value):
    youtube_regex = re.compile(
        r'^(https?://)?(www\.)?(youtube|youtu|youtube-nocookie)\.(com|be)/'
        r'(watch\?v=|embed/|v/|.+\?v=)?([^&=%\?]{11})')
    if not youtube_regex.match(value):
        raise ValidationError('Esta não é uma URL válida do YouTube.')

class VideoURL(models.Model):
    url = models.URLField(
        max_length=200,
        validators=[URLValidator(), validate_youtube_url],
        unique=True,
    )
    added_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.url
