# Generated by Django 2.1.7 on 2019-03-19 00:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0012_auto_20190319_0229'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='is_approved',
            field=models.BooleanField(default=False, verbose_name='Approved?'),
        ),
    ]
