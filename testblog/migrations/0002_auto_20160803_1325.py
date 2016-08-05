# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('testblog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='author_id',
        ),
        migrations.AddField(
            model_name='post',
            name='usermame',
            field=models.CharField(max_length=50, default='none'),
            preserve_default=False,
        ),
    ]
