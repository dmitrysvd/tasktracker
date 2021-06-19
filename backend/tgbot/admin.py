from django.contrib import admin
from .models import DailyMailing, TelegramUser


@admin.register(DailyMailing)
class DailyMailingAdmin(admin.ModelAdmin):
    pass


@admin.register(TelegramUser)
class TelegramUserAdmin(admin.ModelAdmin):
    pass
