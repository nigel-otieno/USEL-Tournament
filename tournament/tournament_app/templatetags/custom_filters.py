# templatetags/custom_filters.py
from django import template
from django.utils.safestring import SafeString

register = template.Library()

@register.filter
def youtube_embed(value):
    """
    Converts a YouTube URL to an embed URL.
    Example: https://www.youtube.com/watch?v=dQw4w9WgXcQ -> https://www.youtube.com/embed/dQw4w9WgXcQ
    """
    if "youtube.com" in value:
        return value.replace("watch?v=", "embed/")
    return value


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