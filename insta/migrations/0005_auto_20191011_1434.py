# Generated by Django 2.2.5 on 2019-10-11 11:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('insta', '0004_comment_image_like'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='profile',
        ),
        migrations.RemoveField(
            model_name='like',
            name='image',
        ),
        migrations.RemoveField(
            model_name='like',
            name='person',
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
        migrations.DeleteModel(
            name='Image',
        ),
        migrations.DeleteModel(
            name='Like',
        ),
    ]
