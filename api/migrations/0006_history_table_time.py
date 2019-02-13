# Generated by Django 2.1.1 on 2019-01-28 16:34

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_remove_history_table_date_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='history_table',
            name='time',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]