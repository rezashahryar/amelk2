# Generated by Django 5.1.6 on 2025-02-25 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('models', '0012_alter_amenities_facility_alter_amenities_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='house_type',
            field=models.CharField(choices=[('v', 'ویلا'), ('o', 'اداری'), ('a', 'آپارتمان'), ('h', 'خانه')], max_length=1, null=True, verbose_name='نوع خانه'),
        ),
    ]
