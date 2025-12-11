from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from .models import Post
from .forms import PostForm


def post_list(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'posts/list.html', {'posts': posts})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'posts/detail.html', {'post': post})


def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save()
            return redirect(reverse('posts:detail', args=[post.pk]))
    else:
        form = PostForm()
    return render(request, 'posts/form.html', {'form': form, 'action': 'Create'})


def post_update(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save()
            return redirect(reverse('posts:detail', args=[post.pk]))
    else:
        form = PostForm(instance=post)
    return render(request, 'posts/form.html', {'form': form, 'action': 'Update'})


def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        post.delete()
        return redirect(reverse('posts:list'))
    return render(request, 'posts/confirm_delete.html', {'post': post})
