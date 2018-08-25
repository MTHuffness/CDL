# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('draft', '0002_player_draft_pos'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='year',
            field=models.CharField(verbose_name='Year', max_length=20, blank=True, null=True, default=None),
        ),
    ]
