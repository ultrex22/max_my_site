from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView, View
from django.views.generic.list import ListView
from django.http import HttpResponseRedirect
from django.urls import reverse

from .forms import CommentForm
from .models import Post

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


class SinglePostDetail(View):

    def get(self, request, slug):
        post = Post.objects.get(slug=slug)
        context = {
            "post": post,
            "post_tags": post.tag.all(),
            "comment_form": CommentForm(),
            "comments":post.comments.all().order_by("-id")
        }
        return render(request, 'blog/post-detail.html', context)

    def post(self, request, slug):
        comment_form = CommentForm(request.POST)
        post = Post.objects.get(slug=slug)

        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
            return HttpResponseRedirect(reverse('post-detail-page', args=[slug]))

        else:
            print('invalid form data')
            context = {
                "post": post,
                "post_tags": post.tag.all(),
                "comment_form": comment_form,
                "comments":post.comments.all().order_by("-id")
            }
            return render(request, 'blog/post-detail.html', context)


def get_date(post):
    return post.get("date")

class ReadLaterView(View):
    def post(self, request):
        stored_posts = request.session.get("stored_posts")
        post_id = int(request.POST["post_id"])
        if stored_posts is None:
            stored_posts = []
        
        if post_id not in stored_posts:
            stored_posts.append(post_id)

        return HttpResponseRedirect("/")