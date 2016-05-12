# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-12 14:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import mezzanine.core.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('pages', '0003_auto_20150527_1555'),
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='pages.Page')),
                ('illustration', mezzanine.core.fields.FileField(blank=True, max_length=255, null=True, verbose_name='illustration')),
            ],
            options={
                'ordering': ('_order',),
            },
            bases=('pages.page',),
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='pages.Page')),
                ('illustration', mezzanine.core.fields.FileField(blank=True, max_length=255, null=True, verbose_name='illustration')),
                ('adress', models.CharField(blank=True, max_length=255)),
                ('zipCode', models.CharField(blank=True, max_length=255)),
                ('area', models.CharField(blank=True, max_length=255)),
                ('city', models.CharField(blank=True, max_length=255)),
                ('country', models.CharField(blank=True, max_length=255)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('tel', models.CharField(blank=True, max_length=20)),
                ('fax', models.CharField(blank=True, max_length=20)),
                ('website', models.CharField(blank=True, max_length=20)),
                ('highlight', models.BooleanField(default=False)),
                ('brands', models.ManyToManyField(blank=True, to='MAIN.Brand')),
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
                ('illustration', mezzanine.core.fields.FileField(blank=True, max_length=255, null=True, verbose_name='illustration')),
                ('firstName', models.CharField(blank=True, max_length=255)),
                ('adress', models.CharField(blank=True, max_length=255)),
                ('zipCode', models.CharField(blank=True, max_length=255)),
                ('area', models.CharField(blank=True, max_length=255)),
                ('city', models.CharField(blank=True, max_length=255)),
                ('country', models.CharField(blank=True, max_length=255)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('tel', models.CharField(blank=True, max_length=20)),
                ('highlight', models.BooleanField(default=False)),
                ('companies', models.ManyToManyField(through='MAIN.Job', to='MAIN.Company')),
            ],
            options={
                'ordering': ('_order',),
            },
            bases=('pages.page',),
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='pages.Page')),
                ('illustration', mezzanine.core.fields.FileField(blank=True, max_length=255, null=True, verbose_name='illustration')),
            ],
            options={
                'ordering': ('_order',),
            },
            bases=('pages.page',),
        ),
        migrations.CreateModel(
            name='Subsidiary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.CharField(blank=True, max_length=255)),
                ('sub_company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sub_companies', to='MAIN.Company')),
                ('top_company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='top_companies', to='MAIN.Company')),
            ],
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='pages.Page')),
                ('illustration', mezzanine.core.fields.FileField(blank=True, max_length=255, null=True, verbose_name='illustration')),
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
            name='subsidiaries',
            field=models.ManyToManyField(through='MAIN.Subsidiary', to='MAIN.Company'),
        ),
        migrations.AddField(
            model_name='company',
            name='topics',
            field=models.ManyToManyField(blank=True, to='MAIN.Topic'),
        ),
        migrations.AddField(
            model_name='brand',
            name='products',
            field=models.ManyToManyField(blank=True, to='MAIN.Product'),
        ),
        migrations.AddField(
            model_name='brand',
            name='topics',
            field=models.ManyToManyField(blank=True, to='MAIN.Topic'),
        ),
    ]
