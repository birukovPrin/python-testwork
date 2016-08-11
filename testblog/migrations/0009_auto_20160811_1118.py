# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('testblog', '0008_auto_20160810_1415'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='article',
            field=models.ForeignKey(to='testblog.Post', related_query_name='article'),
        ),
    ]
