# Generated by Django 2.0.6 on 2018-07-11 03:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('departments', '0002_auto_20180628_1703'),
    ]

    operations = [
        migrations.AddField(
            model_name='department',
            name='protected',
            field=models.BooleanField(default=False),
        ),
    ]