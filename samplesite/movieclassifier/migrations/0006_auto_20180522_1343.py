# Generated by Django 2.0.5 on 2018-05-22 04:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movieclassifier', '0005_auto_20180521_1931'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2018, 5, 22, 13, 43, 23, 877136), verbose_name='date published'),
        ),
    ]
