from django.contrib import admin
from .models import Project, Tasks

class TasksAdmin(admin.ModelAdmin):
    readonly_fields = ("created", )

# Register your models here.
admin.site.register(Project)
admin.site.register(Tasks, TasksAdmin)