from django.contrib import admin
from .models import Car, Customer, CarBooking, CarRepairDetail, Mechanic, RepairCostEstimation, PayementDetail, BookingNotification, Workshop


# Register models
admin.site.register(Car)
admin.site.register(Customer)
admin.site.register(CarBooking)
admin.site.register(CarRepairDetail)
admin.site.register(Mechanic)
admin.site.register(RepairCostEstimation)
admin.site.register(PayementDetail)
admin.site.register(BookingNotification)
admin.site.register(Workshop)

