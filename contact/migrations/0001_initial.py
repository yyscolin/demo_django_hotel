# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2020-01-30 07:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=48)),
                ('last_name', models.CharField(blank=True, max_length=48, null=True)),
                ('email', models.CharField(max_length=120)),
                ('country_code', models.PositiveIntegerField(blank=True, null=True)),
                ('phone', models.PositiveIntegerField(blank=True, null=True)),
                ('content', models.TextField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
