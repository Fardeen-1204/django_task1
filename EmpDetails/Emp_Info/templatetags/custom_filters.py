from django import template
register=template.Library()

@register.simple_tag
def cut_string(val,cut_val):
    return val[:cut_val]

register.filter('cut_string',cut_string)
