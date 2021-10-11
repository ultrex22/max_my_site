from django.db import models
from django.core import validators
from django.core.validators import EmailValidator
from django.db.models.base import Model
from django.db.models.fields import CharField, DateField, SlugField
from django.urls import reverse
from django.utils.text import slugify

# Create your models here.

class Post(models.Model):
    title =  models.CharField(max_length=100)
    excerpt =  models.CharField(max_length=255)
    image_name =  models.CharField(max_length=100)
    date =  models.DateField(auto_now=True)
    slug =  models.SlugField(default='', blank=True,
                            null=False, db_index=True, max_length=255)
    content =  models.CharField(max_length=2000)

    # class Meta:
    #     verbose_name_plural = 'Posts'

    def __str__(self):
        return f"{self.title}"

# class Tag(models.Model):
#     name =  models.CharField(max_length=50)

# class Author(models.Model):
#     first_name =  models.CharField(max_length=100)
#     last_name =  models.CharField(max_length=100)
#     email =  models.EmailField( validators=[models.EmailField(_("email"), max_length=254)])
