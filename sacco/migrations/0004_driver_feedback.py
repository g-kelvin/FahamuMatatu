# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-10-10 22:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sacco', '0003_auto_20180912_0841'),
    ]

    operations = [
        migrations.AddField(
            model_name='driver',
            name='feedback',
            field=models.CharField(max_length=1000, null=True),
        ),
    ]