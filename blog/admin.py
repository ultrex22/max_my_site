from django.contrib import admin
from blog import models
from .models import Post
# Register your models here.

admin.site.register(models.Post)


# class PostAdmin(admin.ModelAdmin):
#     # readonly_fields = ('slug',)
#     prepopulated_fields = {'slug': ('slug',)}
#     list_filter = ('title', 'excerpt', 'date', 'image_name', 'slug', 'content')
#     list_display = ('title', 'excerpt', 'date', 'image_name', 'slug', 'content')