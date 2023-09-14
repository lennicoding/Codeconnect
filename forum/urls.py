from django.contrib import admin
from django.urls import path, include
from forum_app import views
from django.conf import settings
from django.conf.urls.static import static

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
    path('profile_photo', views.profile_photo, name="photo"),
    path('view_post/<int:id>/', views.view, name="view"),
    path('answer/<int:post_id>/', views.post_answer, name='post_answer'),
    path('search/', views.search_results, name='search_results'),
]
