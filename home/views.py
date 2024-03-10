from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .models import UserInformation

# Create your views here.
def home(request):
    return render(request,'landingpage/homepage/landing.html')



def user_login(request):
    if request.method=='POST':
        userName = request.POST.get('your_username')
        passWord = request.POST.get('your_password')
        user = authenticate(request,username=userName,password=passWord)
        if user is not None:
            login(request,user)
            return redirect('userhome')
        else:
            return HttpResponse("Username or password is incorrect :(")
    return render(request,'registeration-pages/login-signup/login.html')



def register(request):
    if request.method=='POST':
        userName = request.POST.get('username')
        eMail = request.POST.get('email')
        passWord = request.POST.get('password')
        rePassword = request.POST.get('re_pass')
        if passWord!=rePassword:
            return HttpResponse('Passwords does not match')
        else:
            my_user = User.objects.create_user(userName,eMail,passWord)
            my_user.save()
            my_user_info = UserInformation.objects.create(username = userName,level=1,progress=0)
            my_user_info.save()
            return redirect('login')
    return render(request,'registeration-pages/login-signup/signup.html')



@login_required(login_url='login')
def userhome(request):
    username = request.user.username
    user_profile = UserInformation.objects.get(username=username)
    level = user_profile.level
    progress = user_profile.progress
    context = {'username':username,'level':level,'progress':progress}
    return render(request,'userhome/userhome.html',context)



@login_required(login_url='login')
def user_logout(reuqest):
    logout(reuqest)
    return redirect('login')