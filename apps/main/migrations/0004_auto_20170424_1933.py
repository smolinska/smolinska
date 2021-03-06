# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-24 19:33
from __future__ import unicode_literals

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('photologue', '0010_auto_20160105_1307'),
        ('main', '0003_auto_20170316_2147'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('orderedmodelex_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='main.OrderedModelEx')),
                ('start_date', models.DateField(blank=True, null=True)),
                ('end_date', models.DateField(blank=True, null=True)),
                ('name', models.CharField(max_length=100)),
                ('repository', models.URLField(blank=True, null=True)),
                ('link', models.URLField(blank=True, null=True)),
                ('description', ckeditor.fields.RichTextField(blank=True)),
                ('type', models.PositiveSmallIntegerField(choices=[(0, 'Webpage'), (1, 'Game'), (3, 'Other')])),
                ('images', models.ManyToManyField(blank=True, to='photologue.Photo')),
            ],
            options={
                'ordering': ('order',),
                'abstract': False,
            },
            bases=('main.orderedmodelex',),
        ),
        migrations.CreateModel(
            name='Technology',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('_icon_url', models.URLField()),
                ('icon', models.ImageField(blank=True, null=True, upload_to='tech')),
            ],
            options={
                'verbose_name_plural': 'Technologies',
            },
        ),
        migrations.AddField(
            model_name='project',
            name='technologies',
            field=models.ManyToManyField(blank=True, to='main.Technology'),
        ),
    ]
