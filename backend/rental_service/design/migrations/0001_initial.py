# Generated by Django 2.2.28 on 2023-07-24 04:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Rental',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('booking_number', models.CharField(max_length=10, unique=True)),
                ('customer_name', models.CharField(max_length=100)),
                ('car_category', models.CharField(choices=[('Compact', 'Compact'), ('Premium', 'Premium'), ('Minivan', 'Minivan')], max_length=10)),
                ('rental_date', models.DateTimeField()),
                ('pickup_mileage', models.PositiveIntegerField()),
                ('actual_return_date', models.DateTimeField(blank=True, null=True)),
                ('return_mileage', models.PositiveIntegerField(blank=True, null=True)),
                ('number_of_days', models.PositiveIntegerField(default=0)),
                ('number_of_kilometers', models.PositiveIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='ReturnCar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car_category', models.CharField(choices=[('Compact', 'Compact'), ('Premium', 'Premium'), ('Minivan', 'Minivan')], max_length=10)),
                ('booking_number', models.CharField(max_length=50)),
                ('return_date', models.DateTimeField()),
                ('actual_return_date', models.DateTimeField(blank=True, null=True)),
                ('return_mileage', models.PositiveIntegerField()),
                ('number_of_kilometers', models.PositiveIntegerField(default=0)),
            ],
        ),
    ]