from django.db import models
import datetime

class TaskList(models.Model):
    name=models.CharField(max_length=50)

class Task(models.Model):
    name=models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now=True)
    due_on=models.DateTimeField(auto_now_add=False)
    status=models.CharField(max_length=200)
    task_list=models.ForeignKey(TaskList, on_delete=models.CASCADE)
