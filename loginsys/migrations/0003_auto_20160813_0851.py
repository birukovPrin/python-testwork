# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('loginsys', '0002_auto_20160813_0849'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='phone',
            field=models.CharField(max_length=11, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='skype',
            field=models.CharField(max_length=30, null=True, blank=True),
        ),
    ]
