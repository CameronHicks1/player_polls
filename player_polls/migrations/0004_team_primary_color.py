# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-07 19:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('player_polls', '0003_player_nationality'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='primary_color',
            field=models.CharField(default='', max_length=100),
        ),
    ]
