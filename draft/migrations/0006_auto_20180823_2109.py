# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('draft', '0005_draftorder'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='owner',
            name='pick1',
        ),
        migrations.RemoveField(
            model_name='owner',
            name='pick2',
        ),
        migrations.RemoveField(
            model_name='owner',
            name='pick3',
        ),
    ]
