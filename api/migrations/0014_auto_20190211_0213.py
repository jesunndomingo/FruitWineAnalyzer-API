# Generated by Django 2.1.1 on 2019-02-10 18:13

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0013_auto_20190211_0211'),
    ]

    operations = [
        migrations.AlterField(
            model_name='history_table',
            name='uploaded',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 11, 2, 13, 41, 42713)),
        ),
        migrations.AlterField(
            model_name='update_table',
            name='uploaded',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 11, 2, 13, 41, 25672)),
        ),
    ]
