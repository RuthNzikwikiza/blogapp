from django.shortcuts import render, get_object_or_404
from .models import Post

def post_list(request):
    posts = Post.objects.select_related('author').prefetch_related('comments')
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post.objects.select_related('author').prefetch_related('comments__author'), pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})
