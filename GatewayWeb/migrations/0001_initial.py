# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-06-02 09:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Command',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='name', max_length=100)),
                ('detail', models.CharField(default='details', max_length=1000)),
                ('command', models.CharField(default='whoami', max_length=100)),
            ],
            options={
                'ordering': ('id',),
            },
        ),
    ]
