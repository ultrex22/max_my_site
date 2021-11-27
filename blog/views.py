from django.shortcuts import render, get_object_or_404
from .models import Post

all_posts = Post.objects.all().order_by('-date')


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
    # this will generate a 404 page if item not found. saves from wrapping in a try block.
    id_post = get_object_or_404(Post, slug=slug)
    # this was my soultion, copied from somewhere using next()
    # id_post = next(post for post in all_posts if post.slug == slug)
    return render(request, 'blog/post-detail.html', {
        'post': id_post,
        "post_tags": id_post.tag.all()
    })


def get_date(post):
    return post.get("date")
