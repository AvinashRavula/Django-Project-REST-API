from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class ToDoList(models.Model):
    title = models.CharField(max_length=128)
    task_completed = models.BooleanField()
    user = models.ForeignKey(User, models.CASCADE)

    def __str__(self):
        return self.title