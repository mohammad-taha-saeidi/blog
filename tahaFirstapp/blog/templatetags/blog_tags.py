from django import template
from ..models import Post
register = template.Library()
@register.simple_tag(name = "tp")
def total_post():
    return Post.published.count()
