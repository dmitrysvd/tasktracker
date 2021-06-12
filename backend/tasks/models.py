from django.conf import settings
from django.db import models
from django.db.models import UniqueConstraint


class Role(models.Model):
    READ_ONLY = 'ro'
    READ_WRITE = 'rw'
    PERMISSION_CHOICES = (
        (READ_ONLY, 'Read only'),
        (READ_WRITE, 'Read and write'),
    )

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        verbose_name='Пользователь',
        on_delete=models.CASCADE
    )
    task_group = models.ForeignKey(
        'TaskGroup',
        verbose_name='Список задач',
        on_delete=models.CASCADE
    )
    permission = models.CharField(max_length=20, choices=PERMISSION_CHOICES)

    class Meta:
        verbose_name = 'Участник'
        verbose_name_plural = 'Участники'
        constraints = [
            UniqueConstraint(
                fields=['task_group', 'user'],
                name='role__unique_user_and_task_group'
            ),
        ]


class TaskGroup(models.Model):
    name = models.CharField(verbose_name='Название', max_length=150)

    class Meta:
        verbose_name = 'Список задач'
        verbose_name_plural = 'Списки задач'


class Task(models.Model):
    name = models.CharField(verbose_name='Название', max_length=150)
    description = models.TextField(verbose_name='Описание')
    due_time = models.DateTimeField(
        verbose_name='Время истечения',
        null=True,
        blank=True
    )

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'
