from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import *


@api_view(['GET'])
def users_get(request):
    users1 = users.objects.all()
    serializer = userSerializer(users1, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def users_post(request, format=None):
    serializer = userSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
def users_put(request, pk):
    users1 = users.objects.get(user_id=pk)
    serializer = userSerializer(instance=users1, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def users_delete(request, pk):
    users1 = users.objects.get(user_id=pk)
    users1.delete()
    return Response('Item successfully deleted')


@api_view(['GET'])
def tasks_get(self, request):
    tasks1 = tasks.objects.all()
    serializer = taskSerializer(tasks1, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def tasks_post(request, format=None):
    serializer = taskSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
def tasks_put(request, pk):
    tasks1 = tasks.objects.get(task_id=pk)
    serializer = taskSerializer(instance=tasks1, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def tasks_delete(request, pk):
    tasks1 = tasks.objects.get(task_id=pk)
    tasks1.delete()
    return Response('Item successfully deleted')


@api_view(['GET'])
def goals_get(self, request):
    goals1 = goals.objects.all()
    serializer = goalSerializer(goals1, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def goals_post(request, format=None):
    serializer = goalSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
def goals_put(request, pk):
    goals1 = goals.objects.get(goal_id=pk)
    serializer = goalSerializer(instance=goals1, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def goals_delete(request, pk):
    goals1 = goals.objects.get(goal_id=pk)
    goals1.delete()
    return Response('Item successfully deleted')


@api_view(['GET'])
def userGoals_get(self, request):
    userGoals1 = userGoals.objects.all()
    serializer = userGoalsSerializer(userGoals1, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def userGoals_post(request, format=None):
    serializer = userGoalsSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# @api_view(['PUT'])
# def goals_put(request, pk):
#     userGoals1 = userGoals.objects.get(goal_id=pk)
#     serializer = userGoalsSerializer(instance=userGoals1, data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# @api_view(['DELETE'])
# def goals_delete(request, pk):
#     userGoal1 = userGoals.objects.get(goal_id=pk)
#     userGoal1.delete()
#     return Response('Item successfully deleted')

@api_view(['GET'])
def login_get(self, request):
    login1 = login.objects.all()
    serializer = loginSerializer(login1, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def login_post(request, format=None):
    serializer = loginSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
def login_put(request, pk):
    login1 = login.objects.get(username=pk)
    serializer = loginSerializer(instance=login1, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def login_delete(request, pk):
    login1 = login.objects.get(username=pk)
    login1.delete()
    return Response('Item successfully deleted')


@api_view(['GET'])
def friends_get(self, request):
    friends1 = friends.objects.all()
    serializer = friendsSerializer(friends1, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def friends_post(request, format=None):
    serializer = friendsSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# @api_view(['PUT'])
# def friends_put(request, pk):
#     friends1 = friends.objects.get(username=pk)
#     serializer = friendsSerializer(instance=friends1, data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# @api_view(['DELETE'])
# def friends_delete(request, pk):
#     friends1 = friends.objects.get(username=pk)
#     friends1.delete()
#     return Response('Item successfully deleted')


@api_view(['GET'])
def challenges_get(self, request):
    challenges1 = challenges.objects.all()
    serializer = challengesSerializer(challenges1, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def challenges_post(request, format=None):
    serializer = challengesSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
def challenges_put(request, pk):
    challenges1 = challenges.objects.get(challenge_id=pk)
    serializer = challengesSerializer(instance=challenges1, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def challenges_delete(request, pk):
    challenges1 = challenges.objects.get(challenge_id=pk)
    challenges1.delete()
    return Response('Item successfully deleted')


@api_view(['GET'])
def challengeHistory_get(self, request):
    challengesHistory1 = challengeHistory.objects.all()
    serializer = challengeHistorySerializer(challengesHistory1, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def challengeHistory_post(request, format=None):
    serializer = challengeHistorySerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# @api_view(['PUT'])
# def challengeHistory_put(request, pk):
#     challengeHistory1 = challengeHistory.objects.get(challenge_id=pk)
#     serializer = challengeHistorySerializer(instance=challengeHistory1, data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
# @api_view(['DELETE'])
# def challengeHistory_delete(request, pk):
#     challengeHistory1 = challengeHistory.objects.get(challenge_id=pk)
#     challengeHistory1.delete()
#     return Response('Item successfully deleted')

