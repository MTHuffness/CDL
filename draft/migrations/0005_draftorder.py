# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('draft', '0004_auto_20180823_2003'),
    ]

    operations = [
        migrations.CreateModel(
            name='DraftOrder',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('order', models.IntegerField(verbose_name='Draft Order')),
                ('owner', models.ForeignKey(verbose_name='Owner', blank=True, null=True, default=None, to='draft.Owner')),
            ],
        ),
    ]
