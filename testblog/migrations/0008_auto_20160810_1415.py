# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('testblog', '0007_auto_20160805_1027'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('text', models.TextField()),
            ],
        ),
        migrations.AlterField(
            model_name='post',
            name='username',
            field=models.CharField(max_length=50, default='guest'),
        ),
        migrations.AddField(
            model_name='comments',
            name='article',
            field=models.ForeignKey(to='testblog.Post'),
        ),
    ]
