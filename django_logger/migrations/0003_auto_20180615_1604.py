# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-06-15 23:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_logger', '0002_auto_20170104_1053'),
    ]

    operations = [
        migrations.AlterField(
            model_name='logrelated',
            name='object_id',
            field=models.CharField(max_length=25),
        ),
    ]