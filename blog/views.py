from django.shortcuts import render
from datetime import date
from .models import Post

all_posts = Post.objects.all()


def starting_page(request):
    latest_posts = Post.objects.order_by('-date')[:3]
    return render(request, "blog/index.html", {
        'posts': latest_posts
    })


def posts(request):
    return render(request, 'blog/all-posts.html', {
        'all_posts': all_posts
    })


def post_detail(request, slug):
    id_post = next(post for post in all_posts if post.slug == slug)
    return render(request, 'blog/post-detail.html', {
        'post': id_post,
    })


def get_date(post):
    return post.get("date")
