# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-15 07:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('x509_pki', '0016_auto_20160515_0934'),
    ]

    operations = [
        migrations.AlterField(
            model_name='certificate',
            name='revoked_uuid',
            field=models.UUIDField(default='00000000000000000000000000000001'),
        ),
    ]
