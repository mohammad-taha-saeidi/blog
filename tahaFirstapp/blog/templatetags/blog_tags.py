from django import template
from ..models import Post, Comment

register = template.Library()


@register.simple_tag(name="tp")
def total_post():
    return Post.Published_Manager.count()


@register.simple_tag(name="tc")
def total_comments():
    return Comment.objects.count()


@register.simple_tag(name="lp")
def last_post():
    return Post.Published_Manager.first().published

@register.simple_tag(name="top")
def top_post_comments():
    return Comment.objects.all().order_by('-published_date')[:5]
