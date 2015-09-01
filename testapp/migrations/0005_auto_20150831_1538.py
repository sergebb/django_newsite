# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0004_auto_20150831_1538'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tutorial',
            name='depend_on',
            field=models.ForeignKey(blank=True, to='testapp.Tutorial', null=True),
        ),
    ]
