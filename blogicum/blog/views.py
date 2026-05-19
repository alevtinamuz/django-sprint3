from django.shortcuts import render, get_object_or_404
from django.utils import timezone

from .models import Post, Category


def index(request):
    posts = Post.objects.filter(
        pub_date__lte=timezone.now(),
        is_published=True,
        category__is_published=True
    )[:5]
    return render(request, 'blog/index.html', {'posts': posts})


def post_detail(request, post_id):
    post = get_object_or_404(
        Post,
        id=post_id,
        pub_date__lte=timezone.now(),
        is_published=True,
        category__is_published=True
    )
    return render(
        request,
        'blog/detail.html',
        {'post': post}
    )


def category_posts(request, category_slug):
    category_posts = Post.objects.filter(
        category__slug=category_slug,
        is_published=True,
        pub_date__lte=timezone.now()
    )
    category = get_object_or_404(
        Category,
        slug=category_slug,
        is_published=True
    )
    return render(
        request,
        'blog/category.html',
        {'category_posts': category_posts, 'category': category}
    )
