# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-04-09 11:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0003_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=200)),
                ('text', models.CharField(max_length=500)),
                ('published_date', models.DateTimeField(blank=True, null=True)),
            ],
        ),
    ]
