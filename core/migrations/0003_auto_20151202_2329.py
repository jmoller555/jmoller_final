# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_reply'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reply',
            name='text',
        ),
        migrations.AddField(
            model_name='reply',
            name='rate_per_hour_and_course_experience',
            field=models.TextField(null=True, blank=True),
        ),
    ]
