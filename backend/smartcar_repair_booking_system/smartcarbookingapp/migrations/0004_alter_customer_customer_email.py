# Generated by Django 5.0.3 on 2024-05-06 00:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('smartcarbookingapp', '0003_servicetype_alter_carbooking_service_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='customer_email',
            field=models.EmailField(max_length=254),
        ),
    ]