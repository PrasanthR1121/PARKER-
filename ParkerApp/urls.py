from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', index, name="index"),
    path('register/', register, name="register"),
    path('service/', service, name="service"),
    path('location/', location, name="location"),
    path('about/', about, name="about"),
    path('contact/', contact, name="contact"),
    path('faq/', faq, name="faq"),
    path('privacy_policy/', privacy_policy, name="privacy_policy"),
    path('terms_and_conditions/', terms_and_conditions, name="terms_and_conditions"),
    path('bookings/', bookings, name="bookings"),
    path('feedback/', feedback, name="feedback"),
    path('delete_feedback/<int:id>', delete_feedback, name="delete_feedback"),
    path('view_locations/', view_locations, name="view_locations"),
    path('accept/<int:id>', booking_accept, name="accept"),
    path('delete/<int:id>', booking_delete, name="delete"),
    path('subscribe', subscribe, name="subscribe"),
    path('delete_subscribers/<int:id>', delete_subscribers, name="delete_subscribers"),
    path('vacate', vacate, name="vacate"),
    path('user_exp', user_exp, name="user_exp"),
    path('user_feedback', user_feedback, name="user_feedback"),
    path('user_feedback/', view_user_experience, name='user_feedback'),
    path('delete_user_feedback/<int:id>/', delete_user_feedback, name='delete_user_feedback'),
] 