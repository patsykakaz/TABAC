# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-26 20:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MAIN', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='highlight',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
    ]
