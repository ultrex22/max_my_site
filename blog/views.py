from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView
from django.views.generic.list import ListView
from .models import Post
from .forms import CommentForm

all_posts = Post.objects.all().order_by('-date')


class StartingPageView(TemplateView):
    template_name = 'blog/index.html'
    latest_posts = Post.objects.order_by('-date')[:3]

    def get_context_data(self):
        context = super().get_context_data()
        context['posts'] = self.latest_posts
        return context


class PostsView(ListView):
    template_name = 'blog/all-posts.html'
    model = Post

    def get_context_data(self):
        context = super().get_context_data()
        context['all_posts'] = all_posts
        return context


def post_detail(request, slug):
    # this will generate a 404 page if item not found. saves from wrapping in a try block.
    id_post = get_object_or_404(Post, slug=slug)
    # this was my soultion, copied from somewhere using next()
    # id_post = next(post for post in all_posts if post.slug == slug)
    return render(request, 'blog/post-detail.html', {
        'post': id_post,
        "post_tags": id_post.tag.all(),
        "comment_form":CommentForm()
    })


def get_date(post):
    return post.get("date")
