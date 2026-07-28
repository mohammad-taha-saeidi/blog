from django import template
from ..models import Post,Comment
register = template.Library()
@register.simple_tag(name = "tp")
def total_post():
    return Post.Published_Manager.count()
@register.simple_tag(name = "tc")
def total_comments():
    return Comment.objects.count()
