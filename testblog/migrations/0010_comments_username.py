# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('testblog', '0009_auto_20160811_1118'),
    ]

    operations = [
        migrations.AddField(
            model_name='comments',
            name='username',
            field=models.CharField(max_length=50, default='none'),
            preserve_default=False,
        ),
    ]
