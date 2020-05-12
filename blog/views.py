from django.shortcuts import render, get_object_or_404
from .models import BlogProject

def blog(request):
    blogproject = BlogProject.objects.all()
    context={
        'blogproject':blogproject
    }
    return render(request, 'blog/blog.html',context)

def detail(request, blog_id):
    blogs = get_object_or_404(BlogProject, pk=blog_id )
    context = {
        'blog':blogs
    }
    return render(request, 'blog/detail.html', context)
