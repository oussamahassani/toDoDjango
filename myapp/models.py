from django.db import models
from django.contrib.auth.models import User


class Project(models.Model):
    name = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete = models.CASCADE, null=True)

    def __str__(self) -> str:
        return self.name

class Tasks(models.Model):  
    title = models.CharField(max_length=200)
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True, null=True)
    project = models.ForeignKey(Project, on_delete = models.CASCADE)
    done = models.BooleanField(default=False)
    datecompleted = models.DateTimeField(null=True, blank=True)
    important = models.BooleanField(default=False)
    usersesion=models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self) -> str:
        return self.title + ' - ' + self.project.name   

