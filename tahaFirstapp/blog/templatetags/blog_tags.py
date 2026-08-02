from unicodedata import name

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

# @register.simple_tag(name="top")
# def top_post_comments():
#     for post in Post.Published_Manager.all():
#         i = post
#         if post.comment.count()>
@register.inclusion_tag("partials/latest_posts.html" ,name="lpt")
def latest_posts(count=5):
    l_post = Post.Published_Manager.order_by('-published')[:count]
    context = {
        'l_post': l_post,
    }
    return context
#
@register.inclusion_tag("partials/count_post.html" ,name="cp")
def latest_posts(count=5):
    count_post = Post.Published_Manager.order_by('-published')[:count].count()
    context = {
        'count_post': count_post,
    }
    return context
