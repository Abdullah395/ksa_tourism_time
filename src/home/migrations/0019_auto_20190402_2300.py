# Generated by Django 2.1.7 on 2019-04-02 20:00

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0018_auto_20190330_1331'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='last_seen',
            field=models.DateTimeField(default=datetime.datetime(2019, 4, 2, 20, 0, 28, 203448, tzinfo=utc)),
        ),
    ]
