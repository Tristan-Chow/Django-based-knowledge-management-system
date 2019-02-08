# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-11-29 07:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learn', '0010_auto_20171129_1510'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chart',
            name='link',
            field=models.ImageField(upload_to='chart/'),
        ),
        migrations.AlterField(
            model_name='data',
            name='link',
            field=models.FileField(upload_to='data/'),
        ),
        migrations.AlterField(
            model_name='file',
            name='link',
            field=models.FileField(upload_to='file/'),
        ),
    ]