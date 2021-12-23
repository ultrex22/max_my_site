from django.db import models
# from django.core import validators
# from django.core.validators import EmailValidator
# from django.db.models.base import Model
# from django.db.models.fields import CharField, DateField, SlugField
from django.urls import reverse
from django.utils.text import slugify
from django.core.validators import MinLengthValidator


class Tag(models.Model):
    caption = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.caption}"


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)

    def __str__(self):
        return f"{self.last_name}, {self.first_name}"


class Post(models.Model):
    title = models.CharField(max_length=100)
    excerpt = models.CharField(max_length=255)
    image_name = models.CharField(max_length=100)  
    date = models.DateField(auto_now=True)
    slug = models.SlugField(unique=True)
    content = models.TextField(validators=[MinLengthValidator(10)])
    tag = models.ManyToManyField(Tag)
    author = models.ForeignKey(
        Author, on_delete=models.SET_NULL, null=True, related_name='posts')
