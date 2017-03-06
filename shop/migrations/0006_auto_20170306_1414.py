# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-03-06 11:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_auto_20170226_1931'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='rating_average',
            field=models.FloatField(default=0, editable=False),
        ),
        migrations.AddField(
            model_name='product',
            name='rating_count',
            field=models.IntegerField(default=0, editable=False),
        ),
        migrations.AddField(
            model_name='product',
            name='rating_sum',
            field=models.IntegerField(default=0, editable=False),
        ),
        migrations.AddField(
            model_name='product',
            name='reviews_count',
            field=models.IntegerField(default=0, editable=False),
        ),
    ]
