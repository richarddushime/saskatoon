# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-05-07 19:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0006_notification_is_read'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='newsletter_subscription',
            field=models.BooleanField(default=False, verbose_name='Newsletter subscription'),
        ),
    ]
