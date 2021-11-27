from django.contrib import admin
# from blog import models
from .models import Post, Author, Tag


class PostAdmin(admin.ModelAdmin):
    # readonly_fields = ('slug',)
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('author', 'date', 'title', 'excerpt')
    list_display = ('author', 'title', 'date', 'excerpt')


admin.site.register(Post, PostAdmin)
admin.site.register(Author)
admin.site.register(Tag)
