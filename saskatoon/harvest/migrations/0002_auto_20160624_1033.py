# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-06-24 14:33
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('harvest', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='requestforparticipation',
            name='first_time_picker',
        ),
        migrations.RemoveField(
            model_name='requestforparticipation',
            name='helper_picker',
        ),
    ]
