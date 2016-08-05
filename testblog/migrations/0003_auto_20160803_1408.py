# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('testblog', '0002_auto_20160803_1325'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='usermame',
            new_name='username',
        ),
    ]
