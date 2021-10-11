from django.contrib import admin
# from blog import models
from .models import Post, Author, Tag

# Register your models here.

admin.site.register(Post)
admin.site.register(Author)
admin.site.register(Tag)


class PostAdmin(admin.ModelAdmin):
    # readonly_fields = ('slug',)
    prepopulated_fields = {'slug': ('slug',)}
    list_filter = ('title', 'excerpt', 'date', 'image_name', 'slug', 'content')
    list_display = ('title', 'excerpt', 'date', 'image_name', 'slug', 'content')