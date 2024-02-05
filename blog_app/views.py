from django.shortcuts import render
from .models import Post
from detail_post_app.models import Detail , Category


def blog(request):
    post = Post.objects.all()
    detail = Detail.objects.all()
    category = Category.objects.all()
    return render(request, 'blog_app/blog.html', context={'post': post , 'detail':detail , 'category':category})