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
    path('users/', views.userList.as_view()),
    path('tasks/', views.taskList.as_view()),
    path('goals/', views.goalList.as_view()),
    path('userGoals/', views.userGoalList.as_view()),
    path('login/', views.loginList.as_view()),
    path('friends/', views.friendList.as_view()),
    path('challenges/', views.challengesList.as_view()),
    path('challengeHistory/', views.challengesHistoryList.as_view()),
    path('tasks/', views.taskList.as_view()),
]
