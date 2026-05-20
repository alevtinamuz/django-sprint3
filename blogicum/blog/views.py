from django.shortcuts import render, get_object_or_404
from django.utils import timezone

from .models import Post, Category


ITEMS_PER_PAGE = 5


def get_published_posts():
    return Post.objects.filter(
        pub_date__lte=timezone.now(),
        is_published=True,
        category__is_published=True
    ).select_related('category', 'location')


def index(request):
    posts = get_published_posts()[:ITEMS_PER_PAGE]
    return render(request, 'blog/index.html', {'posts': posts})


def post_detail(request, post_id):
    post = get_object_or_404(
        get_published_posts(),
        id=post_id,
    )
    return render(request, 'blog/detail.html', {'post': post})


def category_posts(request, category_slug):
    category = get_object_or_404(
        Category,
        slug=category_slug,
        is_published=True
    )
    category_posts = category.posts.filter(
        is_published=True,
        pub_date__lte=timezone.now()
    ).select_related('category', 'location')
    return render(
        request,
        'blog/category.html',
        {'category_posts': category_posts, 'category': category}
    )
