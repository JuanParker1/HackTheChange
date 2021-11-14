from django.contrib.postgres.fields import ArrayField
from django.db import models


# Create your models here.
class users(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    user_id = models.AutoField(primary_key=True)
    age = models.IntegerField()
    gender = models.CharField(max_length=10)

    class Meta:
        db_table = 'users'

    def __str__(self):
        return self.first_name


class tasks(models.Model):
    task_id = models.AutoField(primary_key=True)
    task_name = models.IntegerField()
    task_description = models.IntegerField()

    class Meta:
        db_table = 'tasks'

    def __str__(self):
        return self.task_id


class goals(models.Model):
    goal_id = models.AutoField(primary_key=True)
    goal_name = models.IntegerField()
    task_id = models.ForeignKey(tasks, on_delete=models.CASCADE)

    class Meta:
        db_table = 'goals'

    def __str__(self):
        return self.goal_id


class userGoals(models.Model):
    goal_id = models.ForeignKey(goals, on_delete=models.CASCADE)
    user_id = models.ForeignKey(users, on_delete=models.CASCADE)
    # user_goal_id = models.AutoField(primary_key=True)
    progression = models.IntegerField()
    streak = models.IntegerField()

    class Meta:
        db_table = 'userGoals'

    def __str__(self):
        return self.goal_id


class login(models.Model):
    username = models.AutoField(primary_key=True)
    password = models.CharField(max_length=20)
    user_id = models.ForeignKey(users, on_delete=models.CASCADE)

    class Meta:
        db_table = 'login'

    def __str__(self):
        return self.username


class friends(models.Model):
    user_id_1 = models.ForeignKey(users, on_delete=models.CASCADE)
    # friends_list = ArrayField(models.ForeignKey(users, on_delete=models.CASCADE), size=8)

    class Meta:
        db_table = 'friends'

    def __str__(self):
        return self.user_id_1


class challenges(models.Model):
    challenge_id = models.AutoField(primary_key=True)
    user_id_1 = models.ForeignKey(users, on_delete=models.CASCADE)
    # user_id_2 = models.ForeignKey(users, on_delete=models.CASCADE)
    goal_id = models.ForeignKey(goals, on_delete=models.CASCADE)
    time_left_days = models.IntegerField()

    class Meta:
        db_table = 'challenges'

    def __str__(self):
        return self.challenge_id


class challengeHistory(models.Model):
    challenge_id = models.ForeignKey(challenges, on_delete=models.CASCADE)
    user_id_1 = models.ForeignKey(users, on_delete=models.CASCADE)
    # user_id_2 = models.ForeignKey(users, on_delete=models.CASCADE)
    result = models.CharField(max_length=100)

    class Meta:
        db_table = 'challengeHistory'

    def __str__(self):
        return self.challenge_id

