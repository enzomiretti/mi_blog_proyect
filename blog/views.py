from django.shortcuts import render, redirect, get_object_or_404
from .forms import BlogForm  
from .models import Blog  


def home(request):
    return render(request, 'home.html')  


def create_blog(request):
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES) 
        if form.is_valid():
            form.save()
            return redirect('blog_list')  
    else:
        form = BlogForm()
    return render(request, 'create_blog.html', {'form': form})


def blog_list(request):
    blogs = Blog.objects.all()  
    return render(request, 'blog_list.html', {'blogs': blogs}) 


def blog_detail(request, pk):
    blog = get_object_or_404(Blog, pk=pk)  
    return render(request, 'blog_detail.html', {'blog': blog})


def delete_blog(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    if request.method == 'POST':
        blog.delete()
        return redirect('blog_list')  
    return render(request, 'delete_blog.html', {'blog': blog})
