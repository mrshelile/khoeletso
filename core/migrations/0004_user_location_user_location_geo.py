# Generated by Django 4.2.6 on 2023-10-12 04:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_alter_user_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='location',
            field=models.CharField(default={}, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='location_geo',
            field=models.JSONField(default={}),
            preserve_default=False,
        ),
    ]