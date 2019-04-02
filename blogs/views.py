from django.shortcuts import render, get_object_or_404

from .models import Blog

def blogs(request):
    blogs = Blog.objects
    return render(request, 'blogs/blogs.html', {'blogs':blogs})


def blog(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    # blog = {"title":"Really cool article"}
    return render(request, 'blogs/blog.html', {'blog':blog})    