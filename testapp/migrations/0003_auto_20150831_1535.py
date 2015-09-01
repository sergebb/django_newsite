# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0002_auto_20150831_1532'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tutorial',
            name='tutorial_order',
            field=models.IntegerField(blank=True),
        ),
    ]
