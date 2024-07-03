# templatetags/custom_filters.py
from django import template
from django.utils.safestring import SafeString
import re

register = template.Library()

@register.filter
def youtube_embed(value):
    """
    Converts any YouTube URL to an embed URL.
    Handles:
    - https://www.youtube.com/watch?v=dQw4w9WgXcQ
    - https://youtu.be/dQw4w9WgXcQ
    - https://www.youtube.com/embed/dQw4w9WgXcQ
    """
    youtube_id_match = re.search(
        r'(https?://)?(www\.)?(youtube|youtu|youtube-nocookie)\.(com|be)/(watch\?v=|embed/|v/|.+\?v=)?([^&=%\?]{11})', value)
    if youtube_id_match:
        video_id = youtube_id_match.group(6)
        return f"https://www.youtube.com/embed/{video_id}"
    return None

@register.filter
def add(value, arg):
    try:
        return int(value) + int(arg)
    except (ValueError, TypeError):
        return value

@register.filter
def get_item(list, index):
    try:
        return list[index]
    except IndexError:
        return None

@register.filter
def get_next(value):
    return str(int(value) + 1)

@register.filter(name='add_class')
def add_class(value, css_class):
    if hasattr(value, 'as_widget'):
        return value.as_widget(attrs={"class": css_class})
    elif isinstance(value, SafeString):
        return value.replace('class="', f'class="{css_class} ')
    return value