# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('draft', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='draft_pos',
            field=models.IntegerField(verbose_name='Draft Position', blank=True, null=True, default=None),
        ),
    ]
