# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-20 01:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('songslist', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='songs',
            name='song_id',
            field=models.CharField(default=0, max_length=32, verbose_name='歌曲id'),
            preserve_default=False,
        ),
    ]