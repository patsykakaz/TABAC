# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-26 19:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('pages', '0003_auto_20150527_1555'),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='pages.Page')),
                ('adress', models.CharField(max_length=255)),
                ('zipCode', models.CharField(max_length=255)),
                ('area', models.CharField(blank=True, max_length=255)),
                ('city', models.CharField(max_length=255)),
                ('country', models.CharField(max_length=255)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('tel', models.CharField(blank=True, max_length=20)),
            ],
            options={
                'ordering': ('_order',),
            },
            bases=('pages.page',),
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255)),
                ('since', models.DateField(blank=True, null=True)),
                ('until', models.DateField(blank=True, null=True)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MAIN.Company')),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='pages.Page')),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('tel', models.CharField(blank=True, max_length=20)),
                ('companies', models.ManyToManyField(through='MAIN.Job', to='MAIN.Company')),
            ],
            options={
                'ordering': ('_order',),
            },
            bases=('pages.page',),
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='pages.Page')),
            ],
            options={
                'ordering': ('_order',),
            },
            bases=('pages.page',),
        ),
        migrations.AddField(
            model_name='job',
            name='person',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MAIN.Person'),
        ),
        migrations.AddField(
            model_name='company',
            name='topic',
            field=models.ManyToManyField(to='MAIN.Topic'),
        ),
    ]