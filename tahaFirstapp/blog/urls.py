from django.urls import path
from . import views

app_name = 'blog'
urlpatterns = [
    path('',views.index,name='index'),
    path('posts/',views.PostListView.as_view(),name='post'),
    # path('posts/<int:id>',views.post_detail,name='post_detail'),
    path('posts/<pk>', views.PostDetailView.as_view(), name='post_detail'),

]