from django.shortcuts import render , HttpResponse , Http404 , get_object_or_404
from .models import Post
from datetime import datetime
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import  DetailView , ListView

# Create your views here.
def index(request):
    # return HttpResponse("index page")
    return render(request,'parent/base.html')
# def post(request):
#     posts = Post.Published_Manager.all()
#     paginator = Paginator(posts,2)
#     page_number = request.GET.get('page',1)
#     try:
#         posts = paginator.page(page_number)
#     except EmptyPage:
#         posts = paginator.page(paginator.num_pages)
#     except PageNotAnInteger:
#         posts = paginator.page(1)
#     context = {'posts':posts}
#     return render(request,'blog/list.html',context)
class PostListView(ListView):
    context_object_name = 'posts'
    paginate_by = 2
    template_name = 'blog/list.html'
    queryset = Post.Published_Manager.all()
# def post_detail(request,id):
#     # try:
#     #     post = Post.Published_Manager.get(id=id)
#     # except:
#     #     raise Http404("Page not found!")
#     post = get_object_or_404(Post, id=id , status=Post.Status.PUBLISHED)
#     context = {'post':post,
#                # 'date_time':datetime.now(),
#                }
#     return render(request,'blog/detail.html',context)
class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/detail.html'
