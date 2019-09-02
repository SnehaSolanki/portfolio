from django.shortcuts import render, get_object_or_404

from .models import Blog

def projects(request):
    projects = Blog.objects
    return render(request, 'blog/projects.html', {'projects':projects})

def detail(request,blog_id):
    pdetail=get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blog/pdetail.html', {'pdetail':pdetail})
