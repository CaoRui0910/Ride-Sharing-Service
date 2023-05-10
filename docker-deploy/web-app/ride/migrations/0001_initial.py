# Generated by Django 4.1.5 on 2023-02-03 01:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ride',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rideType', models.BooleanField()),
                ('owner', models.IntegerField()),
                ('ownerPassNum', models.IntegerField()),
                ('arrivalTime', models.DateTimeField()),
                ('dest', models.CharField(max_length=128)),
                ('carType', models.CharField(blank=True, default=None, max_length=20, null=True)),
                ('totalPassNum', models.IntegerField()),
                ('specialRequest', models.CharField(blank=True, default=None, max_length=128, null=True)),
                ('status', models.IntegerField(default=0)),
                ('driver', models.IntegerField(blank=True, default=None, null=True)),
                ('shared', models.JSONField(blank=True, default=None, null=True)),
            ],
        ),
    ]
