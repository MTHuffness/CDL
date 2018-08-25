# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('draft', '0006_auto_20180823_2109'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='player',
            name='draft_pos',
        ),
        migrations.RemoveField(
            model_name='player',
            name='owner',
        ),
        migrations.AddField(
            model_name='draftorder',
            name='player',
            field=models.ForeignKey(verbose_name='Player', blank=True, null=True, default=None, to='draft.Player'),
        ),
    ]
