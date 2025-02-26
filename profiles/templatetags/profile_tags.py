from django import template


register = template.Library()

@register.simple_tag
def get_full_path(request):
    return request.build_absolute_uri()
