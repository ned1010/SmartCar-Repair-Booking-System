# Generated by Django 5.0.3 on 2024-03-27 03:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('car_id', models.AutoField(primary_key=True, serialize=False)),
                ('car_number', models.CharField(max_length=100)),
                ('car_company', models.CharField(max_length=100)),
                ('car_model', models.CharField(max_length=100)),
                ('car_year', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('customer_id', models.AutoField(primary_key=True, serialize=False)),
                ('customer_first_name', models.CharField(max_length=100)),
                ('customer_last_name', models.CharField(max_length=100)),
                ('customer_address', models.CharField(max_length=255)),
                ('customer_phone_number', models.CharField(max_length=20)),
                ('customer_email', models.EmailField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Mechanic',
            fields=[
                ('mechanic_id', models.AutoField(primary_key=True, serialize=False)),
                ('mechanic_name', models.CharField(max_length=100)),
                ('mechanic_phone_number', models.CharField(max_length=20)),
                ('mechanic_email', models.EmailField(max_length=100, unique=True)),
                ('mechanic_address', models.CharField(max_length=255)),
                ('mechanic_status', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='RepairCostEstimation',
            fields=[
                ('repair_cost_estimation_id', models.AutoField(primary_key=True, serialize=False)),
                ('repair_type', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('labor_cost', models.DecimalField(decimal_places=2, max_digits=10)),
                ('parts_cost', models.DecimalField(decimal_places=2, max_digits=10)),
                ('total_cost', models.DecimalField(decimal_places=2, max_digits=10)),
                ('estimation_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='CarBooking',
            fields=[
                ('booking_id', models.AutoField(primary_key=True, serialize=False)),
                ('service_type', models.CharField(max_length=100)),
                ('booking_datetime', models.DateTimeField()),
                ('status', models.CharField(max_length=50)),
                ('comments', models.TextField(blank=True)),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='smartcarbookingapp.car')),
                ('mechanic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='smartcarbookingapp.mechanic')),
            ],
        ),
        migrations.CreateModel(
            name='BookingNotification',
            fields=[
                ('booking_notification_id', models.AutoField(primary_key=True, serialize=False)),
                ('notification_type', models.CharField(max_length=50)),
                ('subject', models.CharField(max_length=255)),
                ('message', models.TextField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(default='pending', max_length=20)),
                ('car_booking', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='smartcarbookingapp.carbooking')),
            ],
        ),
        migrations.CreateModel(
            name='CarRepairDetail',
            fields=[
                ('car_repair_id', models.AutoField(primary_key=True, serialize=False)),
                ('repair_labor_cost', models.DecimalField(decimal_places=2, max_digits=10)),
                ('repair_parts_cost', models.DecimalField(decimal_places=2, max_digits=10)),
                ('repair_total_cost', models.DecimalField(decimal_places=2, max_digits=10)),
                ('car_booking', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='smartcarbookingapp.carbooking')),
            ],
        ),
        migrations.AddField(
            model_name='car',
            name='car_customer_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='smartcarbookingapp.customer'),
        ),
        migrations.CreateModel(
            name='PayementDetail',
            fields=[
                ('payement_details_id', models.AutoField(primary_key=True, serialize=False)),
                ('total_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('paid_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('payment_method', models.CharField(max_length=100)),
                ('transaction_id', models.CharField(max_length=100)),
                ('payment_datetime', models.DateTimeField()),
                ('booking', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='smartcarbookingapp.carbooking')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='smartcarbookingapp.customer')),
            ],
        ),
    ]
