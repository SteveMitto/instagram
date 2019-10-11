from django.db import models as md
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Tags(md.Model):
    tag = md.TextField()

    def __str__(self):
        return f'{self.tag}'

    class Meta:
        ordering=['tag']
class Image(md.Model):
    image = md.ImageField(upload_to='articles/')
    name = md.CharField(max_length=70)
    caption = md.TextField()
    profile = md.ForeignKey(User,on_delete=md.CASCADE)
    posted_on = md.DateTimeField(auto_now_add=True)
    tags =md.ManyToManyField(Tags, blank = True)
    def __str__(self):
        return f'{self.name}'

    class Meta:
        ordering=['name']
class Like(md.Model):
    status = md.BooleanField(default=True)
    image = md.ForeignKey(Image ,on_delete=md.CASCADE)
    person = md.ForeignKey(User ,on_delete=md.CASCADE)

    def __str__(self):
        return '{} liked {}'.format(self.person.username, self.image)

    class Meta:
        ordering=['image']

class Comment(md.Model):
    comment=md.TextField()
    image = md.ForeignKey(Image,on_delete=md.CASCADE)
    person = md.ForeignKey(User,on_delete=md.CASCADE)
    posted_on = md.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.person.username}"s comment on {self.image} '

    class Meta:
        ordering=['image']


class Profile(md.Model):
    user = md.OneToOneField(User,on_delete=md.CASCADE)
    name = md.CharField(max_length = 100 ,blank = True)
    profile_pic= md.ImageField(upload_to='profile/',default = 'default.jpg')
    bio =  md.TextField(max_length=500,blank = True)
    acount_stauts= md.BooleanField(default = False ,blank = True)

    @receiver(post_save,sender=User)
    def create_user_profile(sender,instance,created, **kwargs):
        if created:
            Profile.objects.create(user=instanse)

    @receiver(post_save,sender=User)
    def save_user_profile(sender,instance,**kwargs):
        instance.profile.save()

class follows(md.Model):
    follow= md.ForeignKey(User ,on_delete=md.CASCADE , related_name='follows')
    status=md.BooleanField(default=True)
    following = md.ForeignKey(User ,on_delete=md.CASCADE, related_name='followed')

    def __str__(self):
        return f'{follow} follows {following}'
