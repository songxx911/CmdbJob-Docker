# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-29 09:01
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobapp', '0005_customscript'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CustomScript',
        ),
    ]
