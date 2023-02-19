# Generated by Django 4.0 on 2022-12-29 17:37

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Listings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=1000), blank=True, size=None)),
                ('number_of_persons', models.CharField(max_length=100)),
                ('gender', models.CharField(blank=True, max_length=100, null=True)),
                ('map_link', models.CharField(blank=True, max_length=500, null=True)),
                ('location', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('price', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Withdrawal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField(default=0, null=True)),
            ],
        ),
    ]