# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-06 20:35
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('FirstProjectRefactor', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='file',
            field=models.CharField(default=datetime.datetime(2016, 5, 6, 20, 35, 50, 612385, tzinfo=utc), max_length=400),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='person',
            name='birth_date',
            field=models.DateTimeField(default=datetime.datetime(2016, 5, 6, 20, 34, 30, 768574, tzinfo=utc), verbose_name='Birthdate'),
        ),
        migrations.AlterField(
            model_name='post',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2016, 5, 6, 20, 34, 30, 769570, tzinfo=utc), verbose_name='date published'),
        ),
    ]