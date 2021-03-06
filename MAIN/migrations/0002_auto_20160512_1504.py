# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-12 15:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('MAIN', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='subsidiary',
            old_name='link',
            new_name='relationship',
        ),
        migrations.AddField(
            model_name='subsidiary',
            name='relationship_alt',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='subsidiary',
            name='sub_company',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sub_companies', to='MAIN.Company', verbose_name='Soci\xe9t\xe9s affili\xe9es'),
        ),
    ]
