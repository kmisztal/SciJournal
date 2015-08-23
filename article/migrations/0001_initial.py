# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django_fsm
import publications.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Publication',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=512)),
                ('authors', models.CharField(help_text=b'List of authors separated by commas or <i>and</i>.', max_length=2048)),
                ('year', models.PositiveIntegerField()),
                ('month', models.IntegerField(blank=True, null=True, choices=[(1, b'January'), (2, b'February'), (3, b'March'), (4, b'April'), (5, b'May'), (6, b'June'), (7, b'July'), (8, b'August'), (9, b'September'), (10, b'October'), (11, b'November'), (12, b'December')])),
                ('volume', models.IntegerField(null=True, blank=True)),
                ('number', models.IntegerField(null=True, verbose_name=b'Issue number', blank=True)),
                ('pages', publications.fields.PagesField(max_length=32, blank=True)),
                ('note', models.CharField(max_length=256, blank=True)),
                ('keywords', models.CharField(help_text=b'List of keywords separated by commas.', max_length=256, blank=True)),
                ('url', models.URLField(help_text=b'Link to PDF or journal page.', verbose_name=b'URL', blank=True)),
                ('doi', models.CharField(max_length=128, verbose_name=b'DOI', blank=True)),
                ('abstract', models.TextField(blank=True)),
                ('state', django_fsm.FSMField(default=b'new', max_length=50)),
            ],
            options={
                'ordering': ['-year', '-month', '-id'],
                'verbose_name_plural': 'Articles',
            },
        ),
    ]
