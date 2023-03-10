# Generated by Django 4.0 on 2023-01-06 01:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landlords', '0004_listings_property_type_listings_time_to_gsl_bike_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='listings',
            name='time_to_ug_bike',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='listings',
            name='time_to_ug_car',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='listings',
            name='time_to_ug_walk',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]
