# main/templatetags/my_tags.py

import datetime
from django import template
from django.utils.html import conditional_escape
from django.utils.safestring import mark_safe

register = template.Library()


@register.filter()
def mymedia(value):
    if value:
        return f'/media/{value}'

    return '/static/images/shrek.webp'
