# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-10 12:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20170210_1152'),
    ]

    operations = [
        migrations.AddField(
            model_name='fathers',
            name='region_of_birth',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='mothers',
            name='region_of_birth',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='person',
            name='region',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='person',
            name='region_of_birth',
            field=models.TextField(blank=True, null=True),
        ),
    ]
