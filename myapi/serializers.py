from rest_framework import serializers

from .models import *


class userSerializer(serializers.ModelSerializer):
    class Meta:
        model = users
        fields = '__all__'


class taskSerializer(serializers.ModelSerializer):
    class Meta:
        model = tasks
        fields = '__all__'


class goalSerializer(serializers.ModelSerializer):
    class Meta:
        model = goals
        fields = '__all__'


class userGoalsSerializer(serializers.ModelSerializer):
    class Meta:
        model = userGoals
        fields = '__all__'


class loginSerializer(serializers.ModelSerializer):
    class Meta:
        model = login
        fields = '__all__'


class friendsSerializer(serializers.ModelSerializer):
    class Meta:
        model = friends
        fields = '__all__'


class challengesSerializer(serializers.ModelSerializer):
    class Meta:
        model = challenges
        fields = '__all__'


class challengeHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = challengeHistory
        fields = '__all__'
