from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import CarBooking,Customer,Car,Mechanic,Workshop
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.core.exceptions import ValidationError
from django.contrib import messages

# Create your views here.
def index(request):    
    return render(request, 'smartcarbookingapp/index.html')

# Create bookings for car repair or service
def booking_application_form(request):
    if request.method == 'POST':

        # Created instances of CarBooking, Customer, and Car
        car_booking = CarBooking()
        customer = Customer()
        car = Car()

        # Assigning values to the instances
        car_booking.service_type = request.POST.get('service_types')
        car_booking.booking_date = request.POST.get('date')
        car_booking.booking_time = request.POST.get('time')
        customer.customer_first_name = request.POST.get('first_name')
        customer.customer_last_name = request.POST.get('last_name')
        customer.customer_email = request.POST.get('email')
        customer.customer_phone_number = request.POST.get('phone')
        car.car_company = request.POST.get('make')
        car.car_model = request.POST.get('model')
        car.car_year = request.POST.get('year')
        car_booking.comments = request.POST.get('message')
     
        customer.save()   
        car.car_customer_id = customer
        car.save()
        car_booking.car = car
        car_booking.customer = customer
        car_booking.save()

        return render(request, 'smartcarbookingapp/booking_success.html')        
    
    else:
        return render(request, 'smartcarbookingapp/booking_form.html')

# User login function
def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)            
            return redirect('user_appointments') 
        else:
            error_message = 'Invalid username or password'
            return render(request, 'smartcarbookingapp/login_page.html', {'error': error_message})
    else:
        return render(request, 'smartcarbookingapp/login_page.html')

# User signup function
def user_signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password != confirm_password:
            messages.error(request, "Passwords do not match.")
            return render(request, 'smartcarbookingapp/signup.html', {'error': "Passwords do not match."})

        try:
            if User.objects.filter(username=username).exists():
                raise ValidationError("Username already exists.")
            if User.objects.filter(email=email).exists():
                raise ValidationError("Email already exists.")

            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()
            return redirect('login_page')
        except ValidationError as e:
            messages.error(request, str(e))
            return render(request, 'smartcarbookingapp/signup.html', {'error': str(e)})
        except Exception as e:
            messages.error(request, "An unexpected error occurred.")
            return render(request, 'smartcarbookingapp/signup.html', {'error': "An unexpected error occurred."})

    return render(request, 'smartcarbookingapp/signup.html')


# show list of mechanics
def mechanic_details(request):
    data = Mechanic.objects.all()
    return render(request,'smartcarbookingapp/mechanic_profile.html', {'data':data})


# show list of workshops
def workshop_details(request):
    data = Workshop.objects.all()
    return render(request,'smartcarbookingapp/workshop_detail.html', {'data':data})

# Function to logout from application
def user_logout(request):
    return render(request, 'smartcarbookingapp/index.html')


#Function to get the loged in user appointments
def user_appointments(request):    
    user_bookings = CarBooking.objects.filter(car__car_customer_id__customer_email=request.user.email)
    request.user.is_authenticated
    return render(request, 'smartcarbookingapp/user_appointments.html', {'bookings': user_bookings})

