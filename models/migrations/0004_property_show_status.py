# Generated by Django 5.1.6 on 2025-02-24 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('models', '0003_property_house_plan'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='show_status',
            field=models.BooleanField(default=True),
        ),
    ]
