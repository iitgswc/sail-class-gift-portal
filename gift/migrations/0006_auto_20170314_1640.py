# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-14 11:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gift', '0005_auto_20170314_1638'),
    ]

    operations = [
        migrations.AlterField(
            model_name='option',
            name='description',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='option',
            name='img_path',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='remember_token',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
