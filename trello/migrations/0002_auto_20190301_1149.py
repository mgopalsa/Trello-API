# Generated by Django 2.1.7 on 2019-03-01 00:49

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('trello', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='card',
            name='Description',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='card',
            name='Due_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='card',
            name='Label',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='card',
            name='Members',
            field=models.ForeignKey(blank=True, default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='card',
            name='title',
            field=models.CharField(max_length=100),
        ),
    ]