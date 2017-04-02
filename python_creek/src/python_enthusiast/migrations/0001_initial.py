# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SignUp',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('email', models.EmailField(max_length=254)),
                ('first_name', models.CharField(default=b'First Name', max_length=25, null=True, blank=True)),
                ('time_stamp', models.DateTimeField()),
                ('updated', models.DateTimeField(auto_now_add=True)),
                ('upload', models.FileField(upload_to=None)),
            ],
        ),
    ]
