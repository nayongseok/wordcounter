from django.shortcuts import render, get_object_or_404
from .models import Post
def post_read(request, pk):
    post = get_object_or_404(Post, id=pk)
    return render(request,"blog/post_read.html",{'post':post})

def post_list(request):
    posts = Post.objects.all()
    return render(request,"blog/post_list.html",{'list':posts})
# Create your views here.
