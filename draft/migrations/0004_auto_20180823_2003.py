# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('draft', '0003_player_year'),
    ]

    operations = [
        migrations.AddField(
            model_name='owner',
            name='pick1',
            field=models.IntegerField(verbose_name='1st Pick', blank=True, null=True, default=None),
        ),
        migrations.AddField(
            model_name='owner',
            name='pick2',
            field=models.IntegerField(verbose_name='2nd Pick', blank=True, null=True, default=None),
        ),
        migrations.AddField(
            model_name='owner',
            name='pick3',
            field=models.IntegerField(verbose_name='3rd Pick', blank=True, null=True, default=None),
        ),
    ]
