# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('photo', '0002_imagenrechazada'),
    ]

    operations = [
        migrations.AddField(
            model_name='imagenrechazada',
            name='ocultar',
            field=models.BooleanField(default=True),
        ),
    ]
