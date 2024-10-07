from django.core.exceptions import ValidationError
import re

def validate_youtube_url(url):
    youtube_regex = re.compile(
        r'^(https?://)?(www\.)?(youtube|youtu|youtube-nocookie)\.(com|be)/'
        r'(watch\?v=|embed/|v/|.+\?v=)?([^&=%\?]{11})')
    
    if not youtube_regex.match(url):
        raise ValidationError('Esta não é uma URL válida do YouTube.')
