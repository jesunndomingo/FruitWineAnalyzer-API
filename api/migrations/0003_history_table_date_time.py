# Generated by Django 2.1.1 on 2019-01-27 07:50

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20190125_1916'),
    ]

    operations = [
        migrations.AddField(
            model_name='history_table',
            name='date_time',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
