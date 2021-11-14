# """HackTheChange URL Configuration
#
# The `urlpatterns` list routes URLs to views. For more information please see:
#     https://docs.djangoproject.com/en/3.2/topics/http/urls/
# Examples:
# Function views
#     1. Add an import:  from my_app import views
#     2. Add a URL to urlpatterns:  path('', views.home, name='home')
# Class-based views
#     1. Add an import:  from other_app.views import Home
#     2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
# Including another URLconf
#     1. Import the include() function: from django.urls import include, path
#     2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
# """
from django.contrib import admin
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from myapi import views
#
urlpatterns = [
    path('admin/', admin.site.urls),

    path('users_get/', views.users_get.as_view()),
    path('users_post/', views.users_post.as_view()),
    path('users_put/', views.users_put.as_view()),
    path('users_delete/', views.users_delete.as_view()),

    path('tasks_get/', views.tasks_get.as_view()),
    path('tasks_post/', views.tasks_post.as_view()),
    path('tasks_put/', views.tasks_put.as_view()),
    path('tasks_delete/', views.tasks_delete.as_view()),

    path('goals_get/', views.goals_get.as_view()),
    path('goals_post/', views.goals_post.as_view()),
    path('goals_put/', views.goals_put.as_view()),
    path('goals_delete/', views.goals_delete.as_view()),

    path('userGoals_get/', views.userGoals_get.as_view()),
    path('userGoals_post/', views.userGoals_post.as_view()),
    # path('userGoals_put/', views.userGoals_put.as_view()),
    # path('userGoals_delete/', views.userGoals_delete.as_view()),

    path('login_get/', views.login_get.as_view()),
    path('login_post/', views.login_post.as_view()),
    path('login_put/', views.login_put.as_view()),
    path('login_delete/', views.login_delete.as_view()),

    path('friends_get/', views.friends_get.as_view()),
    path('friends_post/', views.friends_post.as_view()),
    # path('friends_put/', views.friends_put.as_view()),
    # path('friends_delete/', views.friends_delete.as_view()),

    path('challenges_get/', views.challenges_get.as_view()),
    path('challenges_post/', views.challenges_post.as_view()),
    path('challenges_put/', views.challenges_put.as_view()),
    path('challenges_delete/', views.challenges_delete.as_view()),

    path('challengeHistory_get/', views.challengeHistory_get.as_view()),
    path('challengeHistory_post/', views.challengeHistory_post.as_view()),
    # path('challengeHistory_put/', views.challengeHistory_put.as_view()),
    # path('challengeHistory_delete/', views.challengeHistory_delete.as_view()),

]
