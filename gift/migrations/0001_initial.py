# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-14 09:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Options',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img_path', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=200)),
                ('price', models.IntegerField(default=0)),
                ('count', models.IntegerField(default=0)),
                ('updated_at', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Transactions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_of_donater', models.IntegerField(default=0)),
                ('webmail_of_donater', models.CharField(max_length=200)),
                ('transactionid', models.IntegerField()),
                ('created_at', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('webmail', models.CharField(max_length=200)),
                ('type', models.IntegerField(default=0)),
                ('choice', models.IntegerField(default=0)),
                ('donation_via_transaction', models.IntegerField(default=0)),
                ('remember_token', models.CharField(max_length=200)),
                ('updated_at', models.DateTimeField()),
            ],
        ),
    ]
