# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-08 19:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('player_polls', '0005_team_secondary_color'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='hometown',
            field=models.CharField(default='Hometown', max_length=200),
        ),
    ]
