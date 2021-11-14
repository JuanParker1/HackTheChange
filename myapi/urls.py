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
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from rest_framework.urlpatterns import format_suffix_patterns
from myapi import views
from django.views.generic import RedirectView

#
urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),

    path('users_get/', views.users_get),
    path('users_post/', views.users_post),
    path('users_put/<str:pk>', views.users_put),
    path('users_delete/<str:pk>', views.users_delete),

    path('tasks_get/', views.tasks_get),
    path('tasks_post/', views.tasks_post),
    path('tasks_put/<str:pk>', views.tasks_put),
    path('tasks_delete/<str:pk>', views.tasks_delete),

    path('goals_get/', views.goals_get),
    path('goals_post/', views.goals_post),
    path('goals_put/<str:pk>', views.goals_put),
    path('goals_delete/<str:pk>', views.goals_delete),

    path('userGoals_get/', views.userGoals_get),
    path('userGoals_post/', views.userGoals_post),
    # path('userGoals_put/<str:pk>', views.userGoals_put),
    # path('userGoals_delete/<str:pk>', views.userGoals_delete),

    path('login_get/', views.login_get),
    path('login_post/', views.login_post),
    path('login_put/<str:pk>', views.login_put),
    path('login_delete/<str:pk>', views.login_delete),

    path('friends_get/', views.friends_get),
    path('friends_post/', views.friends_post),
    # path('friends_put/<str:pk>', views.friends_put),
    # path('friends_delete/<str:pk>', views.friends_delete),

    path('challenges_get/', views.challenges_get),
    path('challenges_post/', views.challenges_post),
    path('challenges_put/<str:pk>', views.challenges_put),
    path('challenges_delete/<str:pk>', views.challenges_delete),

    path('challengeHistory_get/', views.challengeHistory_get),
    path('challengeHistory_post/', views.challengeHistory_post),
    # path('challengeHistory_put/<str:pk>', views.challengeHistory_put),
    # path('challengeHistory_delete/<str:pk>', views.challengeHistory_delete),

]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
