from django.conf import settings
from django.db import models


class TelegramUser(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name='Системный пользователь',
        on_delete=models.CASCADE,
        null=True
    )
    chat_id = models.CharField(
        verbose_name='ID чата с пользователем',
        max_length=50
    )

    def __str__(self):
        return f'Связь пользователя <{self.user.username}> с telegram'

    class Meta:
        verbose_name = 'Пользователь telegram'
        verbose_name_plural = 'Пользователи telegram'


class DailyMailing(models.Model):
    """Рассылка напоминаний и итогов пользователям."""
    REMINDER_MAILING = 'morning'
    FINAL_MAILING = 'evening'
    MAILING_TYPE_CHOICES = (
        (REMINDER_MAILING, 'Напоминание'),
        (FINAL_MAILING, 'Итоговая'),
    )

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name='Адресат',
        on_delete=models.CASCADE,
        null=True
    )
    mailing_type = models.CharField(
        verbose_name='Тип рассылки',
        choices=MAILING_TYPE_CHOICES,
        max_length=15
    )
    # пока не используется
    time = models.TimeField(verbose_name='Время рассылки')
    is_active = models.BooleanField(verbose_name='Активна', blank=True, default=True)

    def __str__(self):
        return (
            f'Рассылка "{self.get_mailing_type_display()}" для {self.user.username} '
        )

    class Meta:
        verbose_name = 'Ежедневная рассылка'
        verbose_name_plural = 'Ежедневные рассылки'
