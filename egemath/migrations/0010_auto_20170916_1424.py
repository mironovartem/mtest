# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-09-16 10:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('egemath', '0009_auto_20170915_0324'),
    ]

    operations = [
        migrations.RenameField(
            model_name='useraccesslevel',
            old_name='user_access_level',
            new_name='user_access_level_ege',
        ),
        migrations.RemoveField(
            model_name='egemathtest',
            name='explanation_text',
        ),
        migrations.AlterField(
            model_name='egemathtest',
            name='access_level',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
