# project/blog/views.py

from django.shortcuts import render, get_object_or_404, redirect
from .models import Blog
from .forms import BlogForm

""" 自作フォーム """
def add_form(request):

    if request.method == "POST":
        form = BlogForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('blog:index')

    else:
        form = BlogForm
    context = {
        'form': form
    }
    return render(request, 'blog/form.html', context)




""" 一覧表示 """
def index(request):
    blogs = Blog.objects.order_by('-id')
    context = {
        'blogs': blogs
    }
    return render(request, 'blog/index.html', context)


""" 詳細表示 """
def detail(request, blog_id):
    blog_text = get_object_or_404(Blog, id=blog_id)
    context = {
        'blog_text': blog_text
    }
    return render(request, 'blog/detail.html', context)

def update(request, pk):
    blog_text = get_object_or_404(Blog, id=pk)

    if request.method == "POST":
        form = BlogForm(request.POST, instance=blog_text)
        if form.is_valid():
            form.save()
            return redirect('blog:update')
    else:
        form = BlogForm(instance=blog_text)
    context = {
        'form': form
    }
    return render(request, 'blog/form.html', context)
