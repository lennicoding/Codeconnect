from django.contrib import admin
from django.urls import path
from forum_app import views

urlpatterns = [
    path('admin/', admin.site.urls, name='admin-interface'),
    path('', views.start, name='start'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('settings/', views.settings, name='settings'),
    path('forum/', views.forum, name='forum'),
    path('profile/', views.profile, name='profile'),
    path('your_questions/', views.your_questions, name='your_questions'),
    path('post_question_title', views.post_question_title, name='post_question_title'),
    path('post_question_description', views.post_question_description, name='post_question_description'),
    path('post_question_tags', views.post_question_tags, name='post_question_tags'),
]
