# Generated by Django 5.1.6 on 2025-02-26 06:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('models', '0017_realstatecompany_avatar'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='homevisitrequest',
            options={'ordering': ('-datetime_created',), 'verbose_name': 'درخواست بازدید خانه', 'verbose_name_plural': 'درخواست های بازدید خانه'},
        ),
    ]
