# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('image', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='names',
            field=models.CharField(default=1, max_length=255, verbose_name='メンバー名'),
            preserve_default=False,
        ),
    ]
