# Generated by Django 2.1.7 on 2019-03-17 15:34

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_auto_20190317_0058'),
    ]

    operations = [
        # migrations.AddField(
        #     model_name='place',
        #     name='opening_hours',
        #     field=models.CharField(default='none', max_length=50),
        #     preserve_default=False,
        # ),
        migrations.AddField(
            model_name='review',
            name='datetime',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
