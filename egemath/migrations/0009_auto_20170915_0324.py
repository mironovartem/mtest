# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-09-14 23:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('egemath', '0008_auto_20170914_1947'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useraccesslevel',
            name='user_access_level',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]