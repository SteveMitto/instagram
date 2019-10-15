from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('',views.home ,name='home'),
    path('signup/',views.signup,name='signup'),
    path('<username>' , views.profile, name='profile'),
    path('unfollow/', views.unfollow),
    path('follow/',views.follow),
    path('like/<img_id>',views.like ,name='like'),
    path('comment/',views.comment,name='comment'),
    path('update/<username>',views.update_profile ,name= 'update_profile'),
    path('update_pic/<username>',views.update_profile_pic , name = 'update_profile_pic')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
