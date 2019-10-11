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
