# Generated by Django 2.2.5 on 2019-10-11 11:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('insta', '0002_likes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='likes',
            name='image',
        ),
        migrations.RemoveField(
            model_name='likes',
            name='person',
        ),
        migrations.DeleteModel(
            name='Image',
        ),
        migrations.DeleteModel(
            name='Likes',
        ),
    ]
