# Generated by Django 5.0.3 on 2024-05-05 23:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('smartcarbookingapp', '0002_remove_carbooking_booking_datetime_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ServiceType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='carbooking',
            name='service_type',
            field=models.CharField(max_length=50),
        ),
    ]