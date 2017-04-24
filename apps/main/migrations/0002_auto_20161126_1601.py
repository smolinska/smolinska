# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-26 16:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='menuitem',
            name='isGallery',
        ),
        migrations.AddField(
            model_name='menuitem',
            name='type',
            field=models.SmallIntegerField(choices=[(0, 'Standard'), (1, 'Gallery')], default=0, verbose_name='Tab type'),
        ),
    ]
