# Generated by Django 3.2.5 on 2021-10-11 00:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20211011_0016'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='image_Name',
            new_name='image_name',
        ),
    ]
