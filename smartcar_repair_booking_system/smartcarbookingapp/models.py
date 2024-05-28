from django.db import models
from django.utils import timezone

# create customer model.
class Customer(models.Model):
    customer_id = models.AutoField(primary_key=True)
    customer_first_name = models.CharField(max_length=100)
    customer_last_name = models.CharField(max_length=100)
    customer_address = models.CharField(max_length=255)
    customer_phone_number =  models.CharField(max_length=20)
    customer_email = models.EmailField()

# Create car model.
class Car(models.Model):
    car_id = models.AutoField(primary_key=True)
    car_number = models.CharField(max_length=100)
    car_customer_id =  models.ForeignKey(Customer, on_delete=models.CASCADE, to_field='customer_id')
    car_company = models.CharField(max_length=100)
    car_model = models.CharField(max_length = 100)
    car_year = models.IntegerField()

# Create mechanic model.
class Mechanic(models.Model):
    mechanic_id = models.AutoField(primary_key=True)
    mechanic_name = models.CharField(max_length=100)
    mechanic_phone_number =  models.CharField(max_length=20)
    mechanic_email = models.EmailField(max_length=100, unique=True)
    mechanic_address =  models.CharField(max_length=255)
    mechanic_status =  models.CharField(max_length=50)

# Create car repair booking model.
class CarBooking(models.Model):
    booking_id = models.AutoField(primary_key=True)    
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    service_type = models.CharField(max_length=50)
    booking_date= models.DateField(default=timezone.now)
    booking_time= models.TimeField(default=timezone.now)
    mechanic = models.ForeignKey(Mechanic, on_delete=models.SET_NULL, null=True)
    status = models.CharField(max_length=50)
    comments = models.TextField(blank=True)

# Create car repair cost estimation model.
class RepairCostEstimation(models.Model):
    repair_cost_estimation_id = models.AutoField(primary_key=True)
    repair_type = models.CharField(max_length=100)
    description = models.TextField()
    labor_cost = models.DecimalField(max_digits=10, decimal_places=2)
    parts_cost = models.DecimalField(max_digits=10, decimal_places=2)
    total_cost = models.DecimalField(max_digits=10, decimal_places=2)
    estimation_date = models.DateField()

# Create car repair details model.
class CarRepairDetail(models.Model):
    car_repair_id = models.AutoField(primary_key=True)
    car_booking = models.ForeignKey(CarBooking, on_delete=models.CASCADE)
    repair_labor_cost = models.DecimalField(max_digits=10, decimal_places=2)
    repair_parts_cost = models.DecimalField(max_digits=10, decimal_places=2)
    repair_total_cost = models.DecimalField(max_digits=10, decimal_places=2)

# Create payement details model.
class PayementDetail(models.Model):
    payement_details_id = models.AutoField(primary_key=True)
    booking = models.ForeignKey(CarBooking, on_delete=models.CASCADE)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    paid_amount = models.DecimalField(max_digits=10, decimal_places=2)    
    payment_method = models.CharField(max_length=100)
    transaction_id = models.CharField(max_length=100)
    payment_datetime = models.DateTimeField()
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)

# Create booking notification model.
class BookingNotification(models.Model):
    booking_notification_id = models.AutoField(primary_key=True)
    car_booking = models.ForeignKey(CarBooking, on_delete=models.CASCADE)    
    notification_type = models.CharField(max_length=50)
    subject = models.CharField(max_length=255)
    message = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, default='pending')


class ServiceType(models.Model):
    name = models.CharField(max_length=100)

 
# Create Workshop model.
class Workshop(models.Model):
    workshop_id = models.AutoField(primary_key=True)
    workshop_name = models.CharField(max_length=100)
    workshop_phone_number =  models.CharField(max_length=20)
    workshop_email = models.EmailField(max_length=100, unique=True)
    workshop_address =  models.CharField(max_length=255)
   







