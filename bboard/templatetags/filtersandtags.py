from django import template

register = template.Library()

@register.filter
def currency(value, cur):
    return f'{value:.1f} {cur}'


register.filter('currency', currency)
