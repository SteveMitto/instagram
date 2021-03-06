from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Image,Like,Comment,Profile,Tags,Follow
from django.http import JsonResponse
from .forms import UpdateProfile,UpdateProfilePhoto,PostImage
# Create your views here.
from django.contrib.auth.decorators import login_required
from django import template
import json
import random
register = template.Library()
@login_required
def home(request):
    images=Image.objects.all()
    following = Follow.objects.filter(follow = request.user)
    likes = Like.objects.all()
    comments = Comment.objects.all()
    try:
        profiles =list(Profile.objects.all().exclude(user = request.user))
        all_profiles = random.sample(profiles,3)
    except ValueError:
        all_profiles =Profile.objects.all().exclude(user = request.user)

    if request.method == "POST":
        form = PostImage(request.POST,request.FILES)
        if form.is_valid():
            image_u =form.cleaned_data['image']
            name =form.cleaned_data['name']
            caption=form.cleaned_data['caption']
            post = Image(image =image_u,name=name,caption = caption,profile = request.user)
            post.save()
            return redirect('home')
    else:
        form = PostImage()
    context={
    'profiles':all_profiles,
    'images':images,
    'following':following,
    'likes':likes,
    'form':form,
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

@login_required
def profile(request,username):
    current_user = User.objects.filter(username = username).first()
    images = Image.objects.filter(profile = current_user )
    try:
        following = Follow.objects.filter(follow = current_user).all()
    except:
        following =[]

    try:
        followers = Follow.objects.filter(following = current_user)
    except Exception as e:
        followers=[]
    follow_status=None
    for follower in followers:
        if request.user == follower.follow:
            print(True)
            follow_status=True
        else:
            print(False)
            follow_status=False

    context={
    'posts':images,
    'current_user':current_user,
    'followers':followers,
    'following':following,
    'follow_status':follow_status
    }
    return render(request,'profile.html',context)

@login_required
def unfollow(request):
    if request.method == 'POST':
        me= request.POST['me']
        you= request.POST['you']
        unfollow = Follow.objects.filter(follow = me ,following = you).first()
        unfollow.delete()
        return JsonResponse({'unfollowed':True})
    return redirect('home')

@login_required
def follow(request):
    if request.method == 'POST':
        me= request.POST['me']
        you= request.POST['you']
        follow = Follow(follow=User.objects.get(pk=me),following=User.objects.get(pk=you))
        follow.save()
        return JsonResponse({'followed':True})
    return redirect('home')

@login_required
def like(request,img_id):
    if request.method == 'GET':
        image = Image.objects.get(pk=img_id)
        already_liked = Like.objects.filter(person = request.user , image = image ).first()
        print(image,'****************',already_liked)
        if already_liked == None:
            liked= Like( image = image, person = request.user)
            liked.save()
            print('********1*********')
            return JsonResponse({'img_id':img_id,'status':True})
        else:
            print('********2*********')
            already_liked.delete()
            return JsonResponse({'img_id':img_id,'status':False})

        print(already_liked)

@login_required
def comment(request):
    if request.method == 'GET':
        image = Image.objects.get(pk = request.GET['imageId'])
        commnent = request.GET['comment']
        comment_s = Comment(person = request.user,comment =commnent,image = image)
        comment_s.save()
        return JsonResponse({'image_id': request.GET['imageId'],'user':request.user.username,'comment':commnent})

@login_required
def update_profile(request,username):
    if request.method == 'POST':
        user = request.user
        form = UpdateProfile(request.POST)
        if form.is_valid():
            name= form.cleaned_data['name']
            bio= form.cleaned_data['bio']
            website= form.cleaned_data['website']
            profile = Profile.objects.get(pk = user.profile.pk)
            profile.name = name
            profile.bio = bio
            profile.website = website
            profile.user = user
            print(profile)
            profile.save()
            return redirect('profile',username)
    else:
        form2 =UpdateProfilePhoto()
        form = UpdateProfile()

    context={
    'form':form,
    'form2':form2
    }

    return render(request,'edit-profile.html',context)

@login_required
def update_profile_pic(request,username):
    if request.method == 'POST':
        form =UpdateProfilePhoto(request.POST,request.FILES)
        if form.is_valid():
            # photo = form.save(commit = False)
            # photo.user = request.user
            photo = form.cleaned_data['profile_pic']
            profile = Profile.objects.get(pk = request.user.profile.pk)
            profile.profile_pic = photo
            profile.save()
            print(photo)

            return redirect('profile',username)
    else:
            return redirect('profile',username)

@login_required
def search(request,search_term):
    results = list(User.objects.filter(username__icontains = search_term))
    res=[]
    for i in results:
        username = i.username
        image = json.dumps("/media/"+str(i.profile.profile_pic))
        name = i.profile.name
        data ={
        'username':username,
        'image':image,
        'name':name
        }
        res.append(data)
    if res:
        return JsonResponse({'results':res})
    else:
        return JsonResponse({'notFound':True,'results':res})

@login_required
def post_details(request,id):
    image = get_object_or_404(Image,pk = id)
    return render(request, 'image-details.html',{'post':image})
