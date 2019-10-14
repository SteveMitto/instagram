from django.contrib import admin
from .models import Image,Like,Comment,Profile,Tags,Follow
# Register your models here.
admin.site.register(Image)
admin.site.register(Profile)
admin.site.register(Comment)
admin.site.register(Tags)
admin.site.register(Follow)
admin.site.register(Like)
