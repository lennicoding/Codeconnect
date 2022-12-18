from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import HttpResponse
from django.template import loader

from .forms import PostForm
from .models import Post

def forum(request):
    current_user = request.user
    all_posts = Post.objects.all()
    return render(request, "forum.html", {'all_posts' : all_posts, 'current_user' : current_user})

def start(request):
    template = loader.get_template('start.html')
    return HttpResponse(template.render())

def login_user(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('forum')
        else:
            messages.success(request, ("There was an error Loggin in, Try Again!"))
            return redirect('login')
    else:
        return render(request, 'login.html', {})

def signup_user(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        login(request, user)
    else:
        messages.success(request, ("There was an error when signing up. Try again, maybe with a new username!"))
    return render(request, "signup.html")

def logout_user(request):
    logout(request)
    messages.success(request, ("You were logged out!"))
    return redirect("login")


def settings(request):
    template = loader.get_template('settings.html')
    return HttpResponse(template.render())

def profile(request):
    template = loader.get_template('profile.html')
    return HttpResponse(template.render())

def your_questions(request):
    template = loader.get_template('your_questions.html')
    return HttpResponse(template.render())

def post_question(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('forum')
    form = PostForm()
    return render(request, "post_question.html", {
        'form': form
    })