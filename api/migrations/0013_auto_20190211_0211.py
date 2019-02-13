# Generated by Django 2.1.1 on 2019-02-10 18:11

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0012_merge_20190211_0210'),
    ]

    operations = [
        migrations.AddField(
            model_name='history_table',
            name='result',
            field=models.CharField(blank=True, max_length=250),
        ),
        migrations.AddField(
            model_name='update_table',
            name='result',
            field=models.CharField(blank=True, max_length=250),
        ),
        migrations.AlterField(
            model_name='history_table',
            name='uploaded',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 11, 2, 11, 47, 175266)),
        ),
        migrations.AlterField(
            model_name='update_table',
            name='uploaded',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 11, 2, 11, 47, 158311)),
        ),
    ]