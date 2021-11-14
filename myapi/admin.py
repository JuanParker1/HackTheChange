from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(users)
admin.site.register(tasks)
admin.site.register(goals)
admin.site.register(userGoals)
admin.site.register(friends)
admin.site.register(challenges)
admin.site.register(challengeHistory)
admin.site.register(login)