from django.urls import path
from Myapp import views

urlpatterns = [
    path('', views.home, name='my_index'),
    path('about', views.about, name='my_about'),
    path('contact', views.contact, name='my_contact'),
    path('call', views.call, name='my_call'),
    path('team', views.team, name='my_team'),
    path('testimonials', views.testimonials, name='my_testimonial'),
    path('facility', views.facility, name='my_facility'),
    path('classes', views.classes, name='my_classes'),
    path('appointment', views.appointment, name='my_appointment')
]