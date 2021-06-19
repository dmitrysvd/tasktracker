from django.core.management.base import BaseCommand
from tgbot.models import DailyMailing
from tgbot import services


class Command(BaseCommand):
    help = 'Отослать сообщения в telegram'  # noqa

    def add_argument(self, parser):
        pass

    def handle(self, *args, **options):
        mailings = DailyMailing.objects.filter(is_active=True)
        for mailing in mailings:
            self.stdout.write(f'Отсылаю сообщение пользователю {mailing.user.username}')
            services.send_morning_message_to_user(user=mailing.user)
