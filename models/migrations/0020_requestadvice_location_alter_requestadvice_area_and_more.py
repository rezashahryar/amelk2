# Generated by Django 5.1.6 on 2025-03-01 01:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('models', '0019_requestadvice_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='requestadvice',
            name='location',
            field=models.CharField(blank=True, max_length=555, null=True),
        ),
        migrations.AlterField(
            model_name='requestadvice',
            name='area',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='requestadvice',
            name='full_name',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='requestadvice',
            name='land_area',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='requestadvice',
            name='land_garage',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='requestadvice',
            name='mobile',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='requestadvice',
            name='num_bathrooms',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='requestadvice',
            name='num_bedrooms',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='requestadvice',
            name='num_garage',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='requestadvice',
            name='num_rooms',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='requestadvice',
            name='year_construction',
            field=models.IntegerField(null=True),
        ),
    ]
