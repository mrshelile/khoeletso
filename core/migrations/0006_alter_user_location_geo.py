# Generated by Django 4.2.6 on 2023-10-12 04:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_alter_user_location_geo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='location_geo',
            field=models.JSONField(default=dict, null=True),
        ),
    ]
