# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-15 07:59
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='catetory',
            new_name='category',
        ),
    ]
