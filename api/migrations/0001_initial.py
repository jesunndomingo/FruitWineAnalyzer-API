# Generated by Django 2.1.1 on 2019-01-24 04:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='fruitwine_table',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ph', models.CharField(max_length=250)),
                ('alcohol_content', models.CharField(max_length=250)),
                ('temperature', models.CharField(max_length=250)),
                ('volatile_acid', models.CharField(max_length=250)),
            ],
        ),
    ]