# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-09-11 20:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('egemath', '0006_auto_20170827_1450'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='egemathtest',
            name='answer_text',
        ),
        migrations.RemoveField(
            model_name='egemathtest',
            name='author',
        ),
        migrations.AlterField(
            model_name='egemathtest',
            name='explanation_video',
            field=models.TextField(blank=True, null=True),
        ),
    ]