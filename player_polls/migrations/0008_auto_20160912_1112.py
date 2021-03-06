# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-12 18:12
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('player_polls', '0007_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='count',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='comment',
            name='player',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='player_polls.Player'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
    ]
