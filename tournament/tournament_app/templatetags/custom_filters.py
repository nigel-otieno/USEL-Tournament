# templatetags/custom_filters.py
from django import template

register = template.Library()


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