# Generated by Django 2.1.7 on 2019-03-17 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_auto_20190317_1936'),
    ]

    operations = [
        # migrations.AddField(
        #     model_name='place',
        #     name='opening_hours',
        #     field=models.CharField(default='none', max_length=50),
        #     preserve_default=False,
        # ),
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(default='/avatars/default-avatar.png', upload_to='avatars/'),
        ),
    ]
