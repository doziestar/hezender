# Generated by Django 3.2.12 on 2022-03-18 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20220318_1223'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='categorymodel',
            name='slug',
        ),
        migrations.RemoveField(
            model_name='eventmodel',
            name='slug',
        ),
        migrations.RemoveField(
            model_name='tagmodel',
            name='slug',
        ),
        migrations.AlterField(
            model_name='blogmodel',
            name='slug',
            field=models.SlugField(max_length=255, unique=True),
        ),
    ]