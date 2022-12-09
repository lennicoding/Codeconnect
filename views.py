from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import HttpResponse
from django.template import loader
from .models import Post, Tag

def forum(request):
    all_posts = Post.objects.all()
    return render(request, "forum.html", {'all_posts' : all_posts})

def start(request):
    template = loader.get_template('start.html')
    return HttpResponse(template.render())

def login_user(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        print("Hello")
        user = authenticate(request, username=username, password=password)
        print("Hello")
        if user is not None:
            login(request, user)
            return redirect('forum')
        else:
            messages.success(request, ("There was an error Loggin in, Try Again!"))
            return redirect('login')
    else:
        return render(request, 'authentication/login.html', {})

def logout_user(request):
    logout(request)
    messages.success(request, ("You were logged out!"))
    return redirect('start')

def signup_user(request):
    return render(request, "signup.html")

def settings(request):
    template = loader.get_template('settings.html')
    return HttpResponse(template.render())

def profile(request):
    template = loader.get_template('profile.html')
    return HttpResponse(template.render())

def your_questions(request):
    template = loader.get_template('your_questions.html')
    return HttpResponse(template.render())

def post_question_title(request):
    template = loader.get_template('post_question_title.html')
    return HttpResponse(template.render())

def post_question_description(request):
    template = loader.get_template('post_questions_description.html')
    return HttpResponse(template.render())

def post_question_tags(request):
    if request.method == "POST":
        print("Received Title: ", request.POST["title"])
        print("Received Description: ", request.POST["description"])
        print("Received Tags: ", request.POST["tags"])
        Post.objects.create(title = request.POST["title"], description = request.POST["description"], tags = request.POST["tags"])

    all_tags = Tag.objects.all()
    return render(request, "post_question_tags.html", {'all_tags' : all_tags})