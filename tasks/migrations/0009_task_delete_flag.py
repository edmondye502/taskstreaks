# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-03-22 19:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0008_auto_20180321_1533'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='delete_flag',
            field=models.BooleanField(default=False),
        ),
    ]