# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-06-21 19:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('harvest', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='requestforparticipation',
            name='confirmation_date',
        ),
        migrations.AddField(
            model_name='requestforparticipation',
            name='acceptation_date',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Accepted on'),
        ),
    ]
