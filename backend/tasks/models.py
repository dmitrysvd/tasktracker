from django.conf import settings
from django.db import models
from django.db.models import UniqueConstraint
from django.utils import timezone


class TaskManager(models.Manager):
    def for_user(self, user):
        return self.filter(task_group__owner=user)

    def active(self, user):
        return self.for_user(user=user).filter(due_dt__gt=timezone.now())


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
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name='Владелец',
        on_delete=models.CASCADE,
        null=True,
    )
    name = models.CharField(verbose_name='Название', max_length=150)

    def __str__(self):
        return f'Список задач "{self.name}"'

    class Meta:
        verbose_name = 'Список задач'
        verbose_name_plural = 'Списки задач'


class Task(models.Model):
    name = models.CharField(verbose_name='Название', max_length=150)
    task_group = models.ForeignKey(
        'TaskGroup',
        verbose_name='Список задач',
        related_name='tasks',
        on_delete=models.CASCADE,
        null=True,
        blank=False
    )
    description = models.TextField(verbose_name='Описание', blank=True)
    due_dt = models.DateTimeField(
        verbose_name='Время истечения',
        null=True,
        blank=True
    )

    objects = TaskManager()

    def __str__(self):
        return f'Задача "{self.name}"'

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'
