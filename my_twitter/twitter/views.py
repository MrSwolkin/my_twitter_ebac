from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Profile, Tweet
from .forms import TweerForm, SignUpForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django import forms

# Create your views here.

def home(request):
    if request.user.is_authenticated:
        form = TweerForm(request.POST or None)
        if request.method == "POST":
            if form.is_valid():
                tweet = form.save(commit=False)
                tweet.user = request.user
                tweet.save()
                messages.success(
                    request, ("Poste realizado com sucesso!"))
                return redirect("home")
            
        tweets = Tweet.objects.all().order_by("-create_at")
        return render(request, "home.html", {"tweets": tweets, "form": form})
    else:
        return render(request, "login.html", {})

def profile_list(request):
    if request.user.is_authenticated:
        profiles = Profile.objects.exclude(user=request.user)
        return render(request, "profile_list.html", {"profiles": profiles})
    else:
        messages.success(request, ("É preciso fazer o Login para ter acesso a essa página"))
        return redirect("home")

def profile(request, pk):
    if request.user.is_authenticated:
        profile = Profile.objects.get(user_id=pk)
        tweets = Tweet.objects.filter(user_id=pk).order_by("-create_at")
        
        if request.method == "POST":
            current_user_profile = request.user.profile
            action = request.POST['follow']
            if action == "unfollow":
                current_user_profile.follows.remove(profile)
            else:
                current_user_profile.follows.add(profile)    
            current_user_profile.save()

        return render(request, "profile.html", {"profile": profile, "tweets": tweets})
    else:
        messages.success(
            request, ("É preciso fazer o Login para ter acesso a essa pagina"))
        return redirect("login")


def login_user(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password )
        if user is not None:
            login(request, user)
            messages.success(request, (f"Login feito com sucesso! Bem-vindo {username}!"))
            return redirect("home")
        else: 
            messages.success(request, ("E-mail ou senha incorretos. Tente novamente!"))
            return redirect("login")
    else:
        return render(request, "login.html", {})

def logout_user(request):
    logout(request)
    messages.success(request, "Até mais!!")
    return redirect("login")


def register_user(request):
    form = SignUpForm()
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password1"]
            
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, (f"Cadastro realizado com sucesso! Bem-vindo {username}!"))
            return redirect("home")
        

    return render(request, "register.html", {"form":form})

def update_user(request):               
    if request.user.is_authenticated:
        if request.method == "POST":
            user_form = UserUpdateForm(request.POST, instance=request.user)
            profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
            
            if user_form.is_valid() and profile_form.is_valid():
                user_form.save()
                profile_form.save()
                return  redirect("home")
            messages.success(
                request, "Atualização realizada com sucesso! ")
        else:
            user_form = UserUpdateForm(instance=request.user)
            profile_form = ProfileUpdateForm()
            
        return render(request, "update_user.html", {"user_form":user_form, "profile_form":profile_form})

    else:    
        messages.success(
            request, ("É preciso fazer o Login para ter acesso a essa página"))
        return redirect("login")
    

def delete_tweet(request, pk):
    tweet = Tweet.objects.get(id=pk)
    if tweet.user == request.user:
        tweet.delete()
        messages.success(
            request, "Tweet deletado com sucesso! ")
        return redirect("home")
    else:
        messages.success(
            request, "Ação não autorizada.")
        return redirect("home")
