# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-03-06 11:42
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0007_auto_20170306_1420'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='comments_count',
        ),
        migrations.RemoveField(
            model_name='product',
            name='rating_average',
        ),
        migrations.RemoveField(
            model_name='product',
            name='rating_count',
        ),
        migrations.RemoveField(
            model_name='product',
            name='rating_sum',
        ),
    ]
