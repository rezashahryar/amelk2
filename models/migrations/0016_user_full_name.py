# Generated by Django 5.1.6 on 2025-02-26 03:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('models', '0015_alter_requestadvice_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='full_name',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
