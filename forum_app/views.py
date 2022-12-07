from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Post
from .models import Tag

def forum(request):
    all_posts = Post.objects.all()
    return render(request, "forum.html", {'all_posts' : all_posts})

def start(request):
    template = loader.get_template('start.html')
    return HttpResponse(template.render())

def signup(request):
    template = loader.get_template('signup.html')
    return HttpResponse(template.render())

def login(request):
    template = loader.get_template('login.html')
    return HttpResponse(template.render())

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