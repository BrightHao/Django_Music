# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-20 02:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('songslist', '0003_auto_20181020_1048'),
    ]

    operations = [
        migrations.AlterField(
            model_name='songs',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
