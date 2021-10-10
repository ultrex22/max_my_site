from django.db import models
from django.core import validators
from django.core.validators import EmailValidator
from django.db.models.base import Model
from django.db.models.fields import CharField, DateField, SlugField
from django.urls import reverse
from django.utils.text import slugify

# Create your models here.

class Post(models.Model):
    Title =  models.CharField(max_length=100)
    Excerpt =  models.CharField(max_length=255)
    Image_Name =  models.CharField(max_length=100)
    Date =  models.DateField(auto_now=True)
    Slug =  models.SlugField(default='', blank=True,
                            null=False, db_index=True, max_length=255)
    Content =  models.CharField(max_length=100)

# class Tag(models.Model):
#     name =  models.CharField(max_length=50)

# class Author(models.Model):
#     first_name =  models.CharField(max_length=100)
#     last_name =  models.CharField(max_length=100)
#     email =  models.EmailField( validators=[models.EmailField(_("email"), max_length=254)])
