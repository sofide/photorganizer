# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('photo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImagenRechazada',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('ruta', models.CharField(max_length=250)),
                ('carpeta', models.ForeignKey(to='photo.Folder')),
            ],
        ),
    ]
