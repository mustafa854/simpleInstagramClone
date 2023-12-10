from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from core.models import Profile



def signin(request):
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username,password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.error(request,'Bad Credentials')
    return render(request, 'signin.html')


def signup(request):
    if request.method == 'POST':
        tandc = request.POST.get('tandc')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        if password1 == password2:
            if tandc == 'on':
                username = request.POST.get('username')
                user = User.objects.filter(username=username)
                if user:
                    messages.error(request, "User already Exists with the chosen username. Login or choose a different username.") 
                else:
                    email = request.POST.get('email')
                    user = User.objects.filter(email=email)
                    if user:
                        messages.error(request, "User already Exists with the chosen email. Login or choose a different email.") 
                    else:
                        new_user = User.objects.create_user(username=username, password=password1,email=email)
                        login(request, new_user)
                        new_profile = Profile.objects.create(user=request.user)
                        
                        return redirect('/')
            else:
                messages.error(request, "Please accept Terms and Conditions!")
                
        else:
            messages.error(request, "Passwords doesn't match!")
        # password = request.POST.get('password')
        # user = authenticate(username=username,password=password)
        # if user is not None:
        #     login(request, user)
        #     return render(request, 'signup.html')
        # else:
        #     messages.error(request,'Bad Credentials')
    return render(request, 'signup.html')


@login_required
def logout_view(request):
    logout(request)
    return redirect('/')