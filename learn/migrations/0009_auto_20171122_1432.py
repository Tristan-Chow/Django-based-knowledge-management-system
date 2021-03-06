# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-11-22 06:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learn', '0008_auto_20171122_1257'),
    ]

    operations = [
        migrations.CreateModel(
            name='Data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('type', models.CharField(max_length=10)),
                ('field', models.CharField(max_length=10)),
                ('dataNo', models.CharField(default=0, max_length=20)),
                ('devotionTime', models.DateField()),
                ('devoter', models.CharField(max_length=20)),
                ('remarks', models.TextField()),
                ('link', models.FileField(upload_to='data/')),
            ],
        ),
        migrations.RenameField(
            model_name='file',
            old_name='modelNo',
            new_name='fileNo',
        ),
    ]
