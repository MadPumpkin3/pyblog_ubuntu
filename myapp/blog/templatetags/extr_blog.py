from django import template
# from django.template.defaultfilters import stringfilter
from django.utils.safestring import mark_safe
from markdownx.utils import markdownify

register = template.Library()

@register.filter
# @stringfilter
def lower(value):
    return value.lower()

@register.filter
def formatted_markdown(text):
    return mark_safe(markdownify(text))