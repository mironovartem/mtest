# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-08-10 19:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('egemath', '0004_auto_20170715_0206'),
    ]

    operations = [
        migrations.AddField(
            model_name='egemathtest',
            name='answer_text',
            field=models.TextField(blank=True, null=True),
        ),
    ]