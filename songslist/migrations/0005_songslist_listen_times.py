# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-30 10:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('songslist', '0004_auto_20181020_1050'),
    ]

    operations = [
        migrations.AddField(
            model_name='songslist',
            name='listen_times',
            field=models.IntegerField(default=0, max_length=16, verbose_name='播放量'),
            preserve_default=False,
        ),
    ]
