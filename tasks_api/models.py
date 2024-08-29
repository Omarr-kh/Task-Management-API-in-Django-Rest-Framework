from django.db import models
from django.contrib.auth.models import User


class Task(models.Model):
    # each task has to be linked with a user
    # all tasks are deleted if the user is deleted
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, blank=False)
    description = models.TextField(blank=False)
    status = models.BooleanField(default=False, verbose_name="completed")
