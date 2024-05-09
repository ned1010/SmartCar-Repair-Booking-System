from django.urls import path
from . import views 

urlpatterns = [
    path("",views.index,name='index'), 
    path("booking",views.booking_application_form,name='booking_application_form'),
    path("login",views.user_login,name="login_page"),
    path("signup",views.user_signup,name="signup"),
    path("mechanic",views.mechanic_details,name="mechanic_profile"),
    path("workshop",views.workshop_details,name="workshop_detail"),
    path('logout', views.user_logout, name='logout'),
    path("appointment",views.user_appointments,name="user_appointments")
]