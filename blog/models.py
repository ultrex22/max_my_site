from django.core.validators import MinLengthValidator
from django.db import models
from django.db.models.deletion import CASCADE


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
    date = models.DateField(auto_now=True)
    image_name = models.ImageField(upload_to='images', null=True)
    slug = models.SlugField(unique=True)
    content = models.TextField(validators=[MinLengthValidator(10)])
    tag = models.ManyToManyField(Tag)
    author = models.ForeignKey(
        Author, on_delete=models.SET_NULL, null=True, related_name='posts')

    def __str__(self) -> str:
        return str(self.title)


class Comment(models.Model):
    user_name = models.CharField(max_length=50)
    user_email = models.EmailField(max_length=255)
    comment = models.TextField(max_length=500)
    post = models.ForeignKey(Post, on_delete=CASCADE, null=True, related_name='comments')

    def __str__(self) -> str:
        return f"By: {self.user_name}, Comment Text: {self.comment}"
