# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0003_auto_20150831_1535'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tutorial',
            name='depend_on',
            field=models.ForeignKey(to='testapp.Tutorial', null=True),
        ),
    ]
