from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Likes, Posts, Profile, Followers
from django.db.models import Q
# Create your views here.


@login_required
def settings(request):
    profile = Profile.objects.get(user=request.user)
    if request.method == 'POST':
        new_profile_image = request.FILES.get('profileImg') 
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        bio = request.POST.get('bio')
        location = request.POST.get('location')
        user = User.objects.get(username=request.user)
        if user.first_name != first_name or user.last_name != last_name:
           user.first_name = first_name
           user.last_name = last_name
           user.save()
        if profile.bio != bio or profile.location != location:
            profile.location = location
            profile.bio = bio
            profile.save()
        #  check for profile image is changed or not
        if new_profile_image:
            profile.profile_img = new_profile_image
            profile.save()  
        return redirect('index')
        
        # profile_img = request.POST.get('profileImg')
        # print(profile.profile_img)
        # print(profile_img)
    
    return render(request, 'setting.html', {'profile':profile})

@login_required
def index(request):
    profile = Profile.objects.get(user=request.user)
    all_profiles = Profile.objects.filter((~Q(user=request.user)))[:5]
    print(all_profiles)
    following = Followers.objects.filter(follower=profile).values("following__user__username")
    all_posts=[]
    for follow in following:
        posts = Posts.objects.filter(user__username=follow['following__user__username'])
        for post in posts:
            all_posts.append(post)   
    user_post = Posts.objects.filter(user=request.user)
    for post in user_post:
        all_posts.append(post)
    return render(request, 'index.html', {'profile':profile, 'posts':reversed(all_posts),'all_profiles':all_profiles})

@login_required
def uploadPost(request):
    if request.method == 'POST':
        postImage = request.FILES.get('postImage')
        postCaption = request.POST.get('postCaption')
        post = Posts.objects.create(img=postImage, caption=postCaption, user=request.user)
        post.save()
        return HttpResponse('ok')
    
# @login_required
# def profile(request, username):
#     profile = Profile.objects.get(user__username=username)
#     posts = Posts.objects.filter(user__username=username)
#     return render(request, 'profile.html', {'profile':profile, 'posts':posts})


from django.shortcuts import get_object_or_404

@login_required
def profile(request, username):
    try:
        profile = Profile.objects.get(user__username=username)
        posts = Posts.objects.filter(user__username=username)
        user_profile = Profile.objects.get(user__username=request.user)
        auth_following = Followers.objects.filter(follower=user_profile).values('following__user__username')
        following_exists = False
        profile_followers = Followers.objects.filter(following=profile).count()
        profile_following = Followers.objects.filter(follower=profile).count()
        for follow in auth_following:
            if follow["following__user__username"] == username:
                following_exists = True
        if str(request.user) == username:
            context={'profile': profile, 'posts': posts, 'following_exists':following_exists, 'profile_followers':profile_followers,'profile_following':profile_following, 'hide_follow':True}
        else:
            context={'profile': profile, 'posts': posts, 'following_exists':following_exists, 'profile_followers':profile_followers,'profile_following':profile_following, 'hide_follow':False}
        return render(request, 'profile.html', context=context )
    except Profile.DoesNotExist:
        # Handle the case where the profile doesn't exist for the given username
        return HttpResponse("Profile not found")

@login_required
def likePost(request, id):
    user = request.user
    post = Posts.objects.get(id=id)
    like_exist = Likes.objects.filter(likedUser=user)
    if like_exist:
        post.likesCount = post.likesCount - 1
        post.save()
        like_exist.delete()
        return redirect('/')
    post.likesCount = post.likesCount + 1
    post.save()
    create_like = Likes.objects.create(likedPost=post,likedUser=user)
    create_like.save()
    return redirect('/')


@login_required
def followUser(request, id):
    print('hi')
    user = request.user.profile
    to_follow = Profile.objects.get(id=id)
    following_exists = Followers.objects.filter(follower=user,following=to_follow)

    print(following_exists)
    if following_exists.exists():
        following_exists.delete()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    following_account = Followers.objects.create(follower=user,following=to_follow)
    following_account.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required
def searchUser(request):
    if request.method == 'POST':
        username = request.POST.get('search-user')
        profile = Profile.objects.filter(user__username__istartswith=username)
    return HttpResponse(profile)
    