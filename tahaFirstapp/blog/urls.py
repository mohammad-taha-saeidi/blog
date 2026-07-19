from django.urls import path
from . import views

app_name = 'blog'
urlpatterns = [
    path('',views.index,name='index'),
    path('posts/',views.post,name='post'),
    path('posts/<int:id>',views.post_detail,name='post_detail'),
]