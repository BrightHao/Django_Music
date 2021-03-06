# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-01-15 06:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Lyric',
            fields=[
                ('songid', models.CharField(max_length=20, primary_key=True, serialize=False, verbose_name='歌曲ID')),
                ('name', models.CharField(max_length=64, verbose_name='歌曲名')),
                ('singer', models.CharField(max_length=64, verbose_name='歌手名')),
                ('lyric', models.CharField(max_length=2048, verbose_name='歌曲歌词')),
            ],
            options={
                'verbose_name_plural': '歌词',
            },
        ),
    ]
