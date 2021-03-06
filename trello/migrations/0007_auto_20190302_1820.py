# Generated by Django 2.1.7 on 2019-03-02 07:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('trello', '0006_auto_20190302_1340'),
    ]

    operations = [
        migrations.AddField(
            model_name='board',
            name='created_by',
            field=models.ForeignKey(blank=True, default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='list',
            name='created_by',
            field=models.ForeignKey(blank=True, default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
