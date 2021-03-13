# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-09-02 04:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Douyin_Song_Rank',
            fields=[
                ('id', models.CharField(max_length=24, primary_key=True, serialize=False, verbose_name='歌曲id')),
                ('name', models.CharField(max_length=64, verbose_name='歌名')),
                ('singer', models.CharField(max_length=10, verbose_name='歌手')),
                ('album', models.CharField(max_length=32, verbose_name='专辑')),
                ('pic_url', models.CharField(max_length=256, verbose_name='歌曲专辑图片')),
                ('sing_url', models.CharField(max_length=256, verbose_name='歌曲链接')),
            ],
            options={
                'verbose_name_plural': '抖音排行榜',
            },
        ),
        migrations.CreateModel(
            name='Hot_Song_Rank',
            fields=[
                ('id', models.CharField(max_length=24, primary_key=True, serialize=False, verbose_name='歌曲id')),
                ('name', models.CharField(max_length=64, verbose_name='歌名')),
                ('singer', models.CharField(max_length=10, verbose_name='歌手')),
                ('album', models.CharField(max_length=32, verbose_name='专辑')),
                ('pic_url', models.CharField(max_length=256, verbose_name='歌曲专辑图片')),
                ('sing_url', models.CharField(max_length=256, verbose_name='歌曲链接')),
            ],
            options={
                'verbose_name_plural': '热歌排行榜',
            },
        ),
        migrations.CreateModel(
            name='New_Song_Rank',
            fields=[
                ('id', models.CharField(max_length=24, primary_key=True, serialize=False, verbose_name='歌曲id')),
                ('name', models.CharField(max_length=64, verbose_name='歌名')),
                ('singer', models.CharField(max_length=10, verbose_name='歌手')),
                ('album', models.CharField(max_length=32, verbose_name='专辑')),
                ('pic_url', models.CharField(max_length=256, verbose_name='歌曲专辑图片')),
                ('sing_url', models.CharField(max_length=256, verbose_name='歌曲链接')),
            ],
            options={
                'verbose_name_plural': '新歌排行榜',
            },
        ),
        migrations.CreateModel(
            name='Popular_Song_Rank',
            fields=[
                ('id', models.CharField(max_length=24, primary_key=True, serialize=False, verbose_name='歌曲id')),
                ('name', models.CharField(max_length=64, verbose_name='歌名')),
                ('singer', models.CharField(max_length=10, verbose_name='歌手')),
                ('album', models.CharField(max_length=32, verbose_name='专辑')),
                ('pic_url', models.CharField(max_length=256, verbose_name='歌曲专辑图片')),
                ('sing_url', models.CharField(max_length=256, verbose_name='歌曲链接')),
            ],
            options={
                'verbose_name_plural': '流行歌排行榜',
            },
        ),
    ]
