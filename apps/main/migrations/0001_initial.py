# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='OrderedModelEx',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('order', models.PositiveIntegerField(editable=False, db_index=True)),
            ],
            options={
                'ordering': ('order',),
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='MenuItem',
            fields=[
                ('orderedmodelex_ptr', models.OneToOneField(auto_created=True, to='main.OrderedModelEx', primary_key=True, parent_link=True, serialize=False)),
                ('title', models.CharField(max_length=50, verbose_name='Title')),
                ('content', ckeditor.fields.RichTextField(blank=True, verbose_name='Content')),
                ('isGallery', models.BooleanField(default=False, verbose_name='Is Gallery')),
            ],
            options={
                'ordering': ('order',),
                'abstract': False,
            },
            bases=('main.orderedmodelex',),
        ),
    ]
