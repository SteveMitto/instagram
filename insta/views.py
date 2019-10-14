from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Image,Like,Comment,Profile,Tags,Follow
from django.http import JsonResponse
# Create your views here.
def home(request):
    images=Image.objects.all()
    following = Follow.objects.filter(follow = request.user)
    likes = Like.objects.all()
    comments = Comment.objects.all()
    context={
    'images':images,
    'following':following,
    'likes':likes,
    'comments':comments
    }
    return render(request,'index.html',context)

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user=form
            form.save()
            return redirect('home')
    else:
        form= UserCreationForm()
    context={
    'form':form
    }
    return render(request,'registration/signup.html', context)

def profile(request,username):
    current_user = User.objects.filter(username = username).first()
    images = Image.objects.all()
    following = Follow.objects.filter(follow = current_user)
    followers = Follow.objects.filter(following = current_user)

    context={
    'posts':images,
    'current_user':current_user,
    'followers':followers,
    'following':following
    }
    return render(request,'profile.html',context)

def unfollow(request):
    if request.method == 'POST':
        me= request.POST['me']
        you= request.POST['you']
        unfollow = Follow.objects.filter(follow = me ,following = you).first()
        unfollow.delete()
        return JsonResponse({'unfollowed':True})
    return redirect('home')

def follow(request):
    if request.method == 'POST':
        me= request.POST['me']
        you= request.POST['you']
        follow = Follow(follow=User.objects.get(pk=me),following=User.objects.get(pk=you))
        follow.save()
        return JsonResponse({'followed':True})
    return redirect('home')

def like(request,img_id):
    if request.method == 'GET':
        image = Image.objects.get(pk=img_id)
        already_liked = Like.objects.filter(person = request.user , image = image ).first()
        print(image,'****************',already_liked)
        if already_liked == None:
            liked= Like( image = image, person = request.user)
            liked.save()
            return JsonResponse({'img_id':img_id,'status':True})
        else:
            already_liked.delete()
            return JsonResponse({'img_id':img_id,'status':False})

        print(already_liked)

def comment(request):
    if request.method == 'GET':
        image = Image.objects.get(pk = request.GET['imageId'])
        commnent = request.GET['comment']
        comment_s = Comment(person = request.user,comment =commnent,image = image)
        comment_s.save()
        return JsonResponse({'image_id': request.GET['imageId'],'user':request.user.username,'comment':commnent})
