# Generated by Django 3.2.4 on 2021-06-19 07:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0002_task_task_group'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='due_time',
            new_name='due_dt',
        ),
    ]