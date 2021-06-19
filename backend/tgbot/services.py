"""Модуль бизнес-логики telegram-бота."""
from django.conf import settings
from django.utils import timezone

from tasks.models import Task

import telegram


def send_telegram_message_to_user(message, user):
    token = settings.TELEGRAM_BOT_TOKEN
    bot = telegram.Bot(token=token)
    chat_id = settings.CHAT_ID  # my testing chat id. Do not use it
    print(message)
    bot.send_message(chat_id=chat_id, text=message)


def send_morning_message_to_user(user):
    # TODO: Перенести в шаблон
    message_lines = [
        'Доброе утро!',
        'Сегодня у вас запланированы следующие задачи:',
    ]
    # TODO: Вынести фильтрацию в менеджер
    user_tasks = Task.objects.filter(due_dt__gt=timezone.now())
    for task in user_tasks:
        message_lines.append(f'- {task.name}')
    message = '\n'.join(message_lines)
    send_telegram_message_to_user(message, user)
