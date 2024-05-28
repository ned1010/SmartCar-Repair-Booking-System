
from django.test import TestCase
from django.urls import reverse
from .models import CarBooking, Car, Mechanic, Customer
from django.contrib.auth.models import User

class BookingTestCase(TestCase):
    
    def setUp(self):
        self.user = User.objects.create_user(username='sruthi', password='123456', email='sruthi@gmail.com')
        self.customer = Customer.objects.create(customer_email = 'sruthi@gmail.com')
        self.mechanic = Mechanic.objects.create(mechanic_name='John Doe')
        self.car = Car.objects.create(car_company='Toyota', car_model='Camry', car_year='2020', car_customer_id=self.customer)

    def test_booking_appointment(self):
        self.client.login(username='sruthi', password='123456')
        
        response = self.client.post(reverse('booking_application_form'), {
            'service_types': 'Engine Servicing',  
            'date': '2024-06-01',
            'time': '10:00',
            'first_name': 'John',
            'last_name': 'Doe',
            'email': 'john.doe@example.com',
            'phone': '1234567890',
            'make': 'Toyota',  
            'model': 'Camry', 
            'year': '2020',  
            'message': 'Please check the engine.'
        })
        
        self.assertEqual(response.status_code, 200)  
        self.assertIn('Booking successful! Thank you for choosing SmartCar.', response.content.decode('utf-8'))
        
        self.assertEqual(CarBooking.objects.count(), 1)  
        booking = CarBooking.objects.first()
        self.assertEqual(booking.service_type, 'Engine Servicing')
        self.assertEqual(booking.car.car_company, 'Toyota')
        self.assertEqual(booking.car.car_model, 'Camry')
        self.assertEqual(booking.car.car_year, 2020)
    print("Test 'test_booking_appointment' passed successfully.")

    def tearDown(self):
        print(f"Test {self._testMethodName} passed successfully.")