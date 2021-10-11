from django.shortcuts import render
from datetime import date
from .models import Post

all_posts = Post.objects.all()

def starting_page(request):
    # sorted_posts = sorted(all_posts, key=Post.date)
    # latest_posts = sorted_posts[-3:]
    return render(request, "blog/index.html", {
        'posts': all_posts
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
