# Generated by Django 4.2.6 on 2023-10-12 04:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_farmer_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='name',
            field=models.CharField(default=None, max_length=200),
            preserve_default=False,
        ),
    ]