# Generated by Django 2.1.7 on 2019-03-02 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trello', '0014_auto_20190302_2217'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='Due_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]