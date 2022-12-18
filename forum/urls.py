from django.contrib import admin
from django.urls import path, include
from forum_app import views

urlpatterns = [
    path('admin/', admin.site.urls, name='admin-interface'),
    path('', views.start, name='start'),
    path('login/', views.login_user, name="login"),
    path('logout/', views.logout_user, name="logout"),
    path('signup/', views.signup_user, name="signup"),
    path('settings/', views.settings, name='settings'),
    path('forum/', views.forum, name='forum'),
    path('profile/', views.profile, name='profile'),
    path('your_questions/', views.your_questions, name='your_questions'),
    path('post_question', views.post_question, name='post_question'),
]
