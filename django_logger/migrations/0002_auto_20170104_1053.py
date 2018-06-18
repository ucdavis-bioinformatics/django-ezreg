# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-01-04 18:53
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('django_logger', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='logrelated',
            name='log',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='related_objects', to='django_logger.Log'),
        ),
    ]