from django.shortcuts import render , HttpResponse , Http404 , get_object_or_404
from .models import Post
from datetime import datetime
# Create your views here.
def index(request):
    # return HttpResponse("index page")
    return render(request,'parent/base.html')
def post(request):
    posts = Post.Published_Manager.all()
    context = {'posts':posts}
    return render(request,'blog/list.html',context)
def post_detail(request,id):
    # try:
    #     post = Post.Published_Manager.get(id=id)
    # except:
    #     raise Http404("Page not found!")
    post = get_object_or_404(Post, id=id , status=Post.Status.PUBLISHED)
    context = {'post':post,
               # 'date_time':datetime.now(),
               }
    return render(request,'blog/detail.html',context)