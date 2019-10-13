from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Image,Like,Comment,Profile,Tags,Follow

# Create your views here.
def home(request):
    return render(request,'index.html')

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
    print(current_user.pk)
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
