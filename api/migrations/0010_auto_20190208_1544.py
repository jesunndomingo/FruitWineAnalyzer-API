# Generated by Django 2.1.1 on 2019-02-08 07:44

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_remove_history_table_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='history_table',
            name='uploaded',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 8, 15, 44, 41, 716376)),
        ),
        migrations.AddField(
            model_name='update_table',
            name='uploaded',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 8, 15, 44, 41, 698356)),
        ),
    ]