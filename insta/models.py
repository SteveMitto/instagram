from django.db import models as md
from django.contrib.auth.models import User

class Image(md.Model):
    image = md.ImageField(upload_to='articles/')
    name = md.CharField(max_length=70)
    caption = md.TextField()
    profile = md.ForeignKey(User,on_delete=md.CASCADE)
    posted_on = md.DateTimeFiled(auto_now_add=True)
    def __str__():
        return f'{name}'

class Likes(md.Model):
    status = md.BooleanField(default=True)
    image = md.ForeignKey(Image ,on_delete=md.CASCADE)
    person = md.ForeignKey(User ,on_delete=md.CASCADE)

    def __str__(self):
        return '{} liked {}'.format(person.username, image)
