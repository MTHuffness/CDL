# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Owner',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(verbose_name='Name', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(verbose_name='Name', max_length=50)),
                ('position', models.CharField(verbose_name='Position', max_length=5)),
                ('team', models.CharField(verbose_name='Team', max_length=20)),
                ('bye', models.IntegerField(verbose_name='Bye')),
                ('rank', models.IntegerField(verbose_name='Rank')),
                ('owner', models.ForeignKey(verbose_name='Owner', blank=True, null=True, default=None, to='draft.Owner')),
            ],
        ),
    ]
