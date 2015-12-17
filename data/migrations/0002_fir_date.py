# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='fir',
            name='date',
            field=models.DateField(default=datetime.date(2015, 12, 17), auto_now_add=True),
            preserve_default=False,
        ),
    ]
