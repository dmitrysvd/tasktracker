from django.contrib import admin
from .models import Role, Task, TaskGroup


@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    pass


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    pass


@admin.register(TaskGroup)
class TaskGroupAdmin(admin.ModelAdmin):
    pass
