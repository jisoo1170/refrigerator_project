# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2019-01-19 08:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_auto_20190119_1723'),
    ]

    operations = [
        migrations.AlterField(
            model_name='food',
            name='unit',
            field=models.CharField(blank=True, choices=[('1', '개'), ('2', 'g'), ('3', 'ml')], max_length=1, null=True),
        ),
    ]
