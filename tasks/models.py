from django.db import models
from django.contrib.auth.models import User


class TaskList(models.Model):
    title = models.CharField(max_length=50)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)


class Task(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    deadline = models.DateField(auto_now=False, auto_now_add=False)
    task_list = models.ForeignKey(
        TaskList, on_delete=models.CASCADE, related_name="tasks"
    )
    done = models.BooleanField(default=False)
