from django.contrib import admin
from .models import DailyMailing


@admin.register(DailyMailing)
class DailyMailingAdmin(admin.ModelAdmin):
    pass
