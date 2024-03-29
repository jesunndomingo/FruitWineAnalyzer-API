# Generated by Django 2.1.1 on 2019-02-10 18:20

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0015_auto_20190211_0216'),
    ]

    operations = [
        migrations.RenameField(
            model_name='history_table',
            old_name='result',
            new_name='rating',
        ),
        migrations.RenameField(
            model_name='update_table',
            old_name='result',
            new_name='rating',
        ),
        migrations.AlterField(
            model_name='history_table',
            name='uploaded',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 11, 2, 20, 11, 473386)),
        ),
        migrations.AlterField(
            model_name='update_table',
            name='uploaded',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 11, 2, 20, 11, 456463)),
        ),
    ]
