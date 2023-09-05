from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.forms import UserCreationForm
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.decorators import login_required
from django.db.models import Q

from .forms import PostForm
from .models import Post, Answer

@login_required
def forum(request):
    current_user = request.user
    if request.method == "POST":
        if request.POST["type"] == "vote":
            obj = Post.objects.get(id=request.POST["id"])
            newCount = obj.vote_count + 1
            Post.objects.filter(id=request.POST["id"]).update(
                vote_count=newCount)
        else:
            Post.objects.filter(id=request.POST["itemId"]).delete()

    all_posts = Post.objects.all().order_by("-vote_count").values()
    return render(request, "forum.html", {'all_posts': all_posts, 'current_user': current_user})


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
            messages.success(
                request, ("There was an error Loggin in, Try Again!"))
            return redirect('login')
    else:
        return render(request, 'login.html', {})


def signup_user(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            messages.success(request, ("Registration Succesfull"))
            login(request, user)
            return redirect("forum")
    else:
        form = UserCreationForm()
    return render(request, "signup.html", {'form': form})


def logout_user(request):
    logout(request)
    messages.success(request, ("You were logged out!"))
    return redirect("login")

@login_required
def settings(request):
    template = loader.get_template('settings.html')
    return HttpResponse(template.render())

@login_required
def profile(request):
    template = loader.get_template('profile.html')
    return HttpResponse(template.render())

@login_required
def your_questions(request):
    all_posts = Post.objects.filter(author=request.user)
    return render(request, "forum.html", {'all_posts': all_posts})

@login_required
def post_question(request):
    current_user = request.user
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('forum')
    form = PostForm()
    return render(request, "post_question.html", {
        'form': form, 'current_user': current_user
    })

@login_required
def view(request, id):
    current_user = request.user
    if request.method == "POST":
        Post.objects.filter(id=id).update(
            description=request.POST["description"], title=request.POST["title"])

    post_obj = Post.objects.get(id=id)
    print(post_obj.title)
    context = {'post': post_obj, 'current_user': current_user}
    return render(request, "view.html", context)


@login_required
def profile_photo(request):
    if request.method == "POST":
        uploaded_file = request.FILES["document"]
        fs = FileSystemStorage()
        fs.save(uploaded_file.name, uploaded_file)
    return render(request, "profile_photo.html")

@login_required
def post_answer(request, post_id):
    if request.method == "POST":
        post = get_object_or_404(Post, id=post_id)
        answer_text = request.POST.get("answer")
        author = request.user

        if answer_text:
            Answer.objects.create(answer=answer_text, post=post, author=author)

    return redirect('forum')



def search_results(request):
    query = request.GET.get('q')

    if query:
        results = Post.objects.filter(Q(title__icontains=query) | Q(description__icontains=query))
    else:
        results = Post.objects.all()

    context = {'results': results}
    return render(request, 'search_results.html', context)
