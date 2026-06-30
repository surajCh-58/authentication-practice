from django.shortcuts import *
from django.db import transaction
from . forms import *
from . models import *
from django.contrib.auth import login, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import *
# Create your views here.
@transaction.atomic
def RegisterView(request,pk=None):
    user_instance=get_object_or_404(User,instance=pk) if pk else None
    profile_instance=get_object_or_404(Profile,instance=user_instance) if user_instance else None
    if request.method=="POST":
        user_form=UserRegistrationForm(request.POST,instance=user_instance)
        profile_form=ProfileRegistrationForm(request.POST,instance=profile_instance)
        
        if user_form.is_valid() and profile_form.is_valid():
            user=user_form.save()
            profile=profile_form.save(commit=False)
            profile.user=user
            profile.save()
            if not pk:
                login(request,user)
                messages.success(request,"f welcome {user.username}! your account has been craeted")
                return redirect("Profile:dashboard")
            else:
                messages.sucess("Profile Updated Sucessfully")
                return redirect("Profile:dashboard")
    else:
            user_form=UserRegistrationForm(instance=user_instance)
            profile_form=ProfileRegistrationForm(instance=profile_instance)
        
    context={
            'u_f':user_form,
            'p_f':profile_form,
            'instance':user_instance
        }
    return render(request,"register.html",context)
    
def LoginView(request):
    if request.user.is_authenticated:
        return redirect("Profile:dashboard")
    if request.method=="POST":
        form=AuthenticationForm(request,data=request.POST)
        if form.is_valid():
            user=form.get_user()
            login(request,user)
            messages.success(request,f"welcome back , {user.username}")
            return redirect("Profile:dashboard")
        else:
            messages.warning(request,"Invalid Username  and password. Please try again") 
    else:
        form=AuthenticationForm()
    return render(request,"login.html",{'form':form})

@login_required
def Dashboard(request):
    return render(request,"dashboard.html")
@login_required
def Logout(request):
    logout(request)
    return redirect("Profile:login")