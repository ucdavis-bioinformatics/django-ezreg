# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-06-18 23:43
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ezreg', '0028_price_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registration',
            name='price',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='registrations', to='ezreg.Price'),
        ),
    ]