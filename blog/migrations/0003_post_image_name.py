# Generated by Django 3.2.5 on 2021-12-24 00:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_remove_post_image_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image_name',
            field=models.ImageField(null=True, upload_to='images'),
        ),
    ]