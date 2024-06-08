# templatetags/custom_filters.py
from django import template

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

