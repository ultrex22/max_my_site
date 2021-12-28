from django.contrib import admin
from django.contrib.admin.filters import ListFilter
# from blog import models
from .models import Comment, Post, Author, Tag


class PostAdmin(admin.ModelAdmin):
    # readonly_fields = ('slug',)
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('author', 'date', 'title', 'excerpt')
    list_display = ('author', 'title', 'date', 'excerpt')

class CommentAdmin(admin.ModelAdmin):
    list_display = ('user_name', 'post', "comment")
    list_filter = ('user_name', 'post', "comment")

admin.site.register(Post, PostAdmin)
admin.site.register(Author)
admin.site.register(Tag)
admin.site.register(Comment, CommentAdmin)
