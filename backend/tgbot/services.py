"""Модуль бизнес-логики telegram-бота."""
from django.conf import settings

from tasks.models import Task
from .models import TelegramUser

import telegram


def send_telegram_message_to_user(message, user):
    token = settings.TELEGRAM_BOT_TOKEN
    bot = telegram.Bot(token=token)
    chat_id = TelegramUser.objects.values_list('chat_id', flat=True).get(user=user)
    print(message)
    bot.send_message(chat_id=chat_id, text=message)


def send_morning_message_to_user(user):
    # TODO: Перенести в шаблон
    message_lines = [
        'Доброе утро!',
        'Сегодня у вас запланированы следующие задачи:',
    ]
    user_tasks = Task.objects.active(user=user)
    for task in user_tasks:
        message_lines.append(f'- {task.name}')
    message = '\n'.join(message_lines)
    send_telegram_message_to_user(message, user)
