# Generated by Django 4.2.3 on 2023-08-11 16:06

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('errand', '0002_alter_errand_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='errand',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 8, 11, 16, 6, 46, 941537, tzinfo=datetime.timezone.utc)),
        ),
    ]
