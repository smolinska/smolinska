from django import template

register = template.Library()


@register.filter
def divide(value, arg):
    try:
        return int(value) // int(arg)
    except (ValueError, ZeroDivisionError):
        return None


@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)
