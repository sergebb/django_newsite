# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tutorial',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tutorial_name', models.CharField(max_length=200)),
                ('tutorial_order', models.IntegerField()),
                ('depend_on', models.ForeignKey(to='testapp.Tutorial')),
            ],
        ),
        migrations.CreateModel(
            name='TutorialGroup',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('group_name', models.CharField(max_length=200)),
                ('group_order', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='tutorial',
            name='tutorial_group',
            field=models.ForeignKey(to='testapp.TutorialGroup'),
        ),
    ]
