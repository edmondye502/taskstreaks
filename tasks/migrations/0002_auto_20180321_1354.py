# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-03-21 20:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tasks',
            name='completed',
            field=models.BooleanField(default=False),
        ),
    ]