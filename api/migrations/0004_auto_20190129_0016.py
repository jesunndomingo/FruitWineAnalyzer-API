# Generated by Django 2.1.1 on 2019-01-28 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_history_table_date_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='history_table',
            name='date_time',
            field=models.DateTimeField(),
        ),
    ]
