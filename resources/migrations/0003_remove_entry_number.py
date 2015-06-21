# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resources', '0002_entry_number'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='entry',
            name='number',
        ),
    ]
