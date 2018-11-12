from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from .models import Post,Profile,Comment
from .forms import PostForm,LocationForm,ProfileForm,CommentForm
from decouple import config,Csv
import datetime as dt

# Create your views here.
def timeline(request):
    posts= Post.objects.all()
    profiles= Profile.objects.all()

    return render(request,'timeline.html',{"posts":posts,"profiles":profiles})

@login_required(login_url='/accounts/login/')
def new_location(request):
    if request.method =='POST':
        form=LocationForm(request.POST,request.FILES)
        if form.is_valid():
            location = form.save(commit=False)
            location.save()

        return redirect('new-post')

    else:
        form = LocationForm()

    return render(request,'new_location.html',{"form":form})

@login_required(login_url='/accounts/login/')
def new_post(request):
    current_user = request.user
    profile = Profile.objects.get(username=current_user)

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.username = current_user
            post.profile_pic = profile.profile_pic

            post.likes=0

            post.save()

        return redirect('Timeline')

    else:
        form = PostForm()

    return render(request,'new_post.html',{"form":form})

@login_required(login_url='/accounts/login/')
def profile(request):
    current_user = request.user
    current_user_id=request.user.id
    print(current_user)
    # print(current_user_id)

    post_id = None
    if request.method == 'GET':
        post_id = request.GET.get('post_id')

    likes = 0
    if post_id:
        post = Post.objects.get(id=int(post_id))
        if post:
            likes = post.likes + 1
            post.likes =  likes
            post.save()
            print(likes)

        return redirect('profile.html')

    try:
        profile = Profile.objects.get(username=current_user)
        posts = Post.objects.filter(username_id=current_user_id)
        title = profile.name
        username = profile.username
        post_number= len(posts)
        # print(post_number)


        if request.method =='POST':
            form=CommentForm(request.POST,request.FILES)
            if form.is_valid():
                comment=form.save(commit=False)
                comment.username=current_user
                comment.post = current_user

                comment.save()

            return redirect('profile')
        else:
            form = CommentForm()

    except ObjectDoesNotExist:
        return redirect('edit-profile')


    return render(request,"profile.html",{"profile":profile,"posts":posts,"form":form,"post_number":post_number,"title":title,"username":username})


@login_required(login_url='/accounts/login/')
def edit_profile(request):
    current_user=request.user
    if request.method =='POST':
        form=ProfileForm(request.POST,request.FILES)
        if form.is_valid():
            profile=form.save(commit=False)
            profile.username = current_user
            profile.save()

    else:
        form=ProfileForm()

    return render(request,'edit_profile.html',{"form":form})


def comment():
    print("AJAX is working")


    return "nothing"

@login_required(login_url='/accounts/login/')
def explore(request):
    posts = Post.objects.all()

    return render(request,"explore.html",{"posts":posts})


@login_required(login_url='/accounts/login/')
def like(request):
    post_id = None
    if request.method == 'GET':
        post_id = request.GET.get('post_id')

    likes = 0
    if post_id:
        post = Post.objects.get(id=int(post_id))
        if post:
            likes = post.likes + 1
            post.likes =  likes
            post.save()
            print(likes)
    return HttpResponse(likes)

@login_required(login_url='/accounts/login/')
def search_results(request):
    if 'user' in request.GET and request.GET["user"]:
        search_term = request.GET.get("user")
        searched_users = Profile.search_profile(search_term)
        message=f"{search_term}"

        return render(request,'search.html',{"message":message,"users":searched_users})

    else:
        message="You haven't searched for any term"
        return render(request,'search.html',{"message":message})

@login_required(login_url='/accounts/login/')
def userprofile(request,profile_id):
    current_user=request.user
    try:
        all_posts=Post.objects.all()
        profile = Profile.objects.get(username=all_post.id)

        posts = Post.objects.filter(username=profile.username)



    except:
        raise ObjectDoesNotExist()
    return render(request,"user-profile.html",{"profile":profile,"posts":posts})
