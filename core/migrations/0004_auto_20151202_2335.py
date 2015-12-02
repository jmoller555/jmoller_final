# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20151202_2329'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reply',
            old_name='rate_per_hour_and_course_experience',
            new_name='course_experience',
        ),
        migrations.AddField(
            model_name='reply',
            name='rate_per_hour',
            field=models.CharField(default=2, max_length=300),
            preserve_default=False,
        ),
    ]
