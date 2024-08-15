from datetime import timedelta

from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from .models import *
from django.http import HttpResponse, Http404
from django.views.decorators.http import require_POST

from django.core.mail import send_mail, EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags

from django.utils.timezone import now
# from django.schedulers import scheduler

def register(request):
    if request.method == 'POST':
        name = request.POST.get("name")
        email = request.POST.get("email")
        pass_1 = request.POST.get("password")
        pass_2 = request.POST.get("re_password")

        if pass_1 == pass_2:
            obj = register_table.objects.create(name=name, email=email, password=pass_1)
            if obj:
                obj.save()
                html_message = render_to_string('email.html', {'variable': 'value'})
                plain_text = strip_tags(html_message)
                email = EmailMultiAlternatives(
                    subject='PARKER',
                    body=plain_text,
                    from_email='prasanthrajan1121@gmail.com',
                    to=[email, "prasanthrajan1121@gmail.com"],
                )
                email.attach_alternative(html_message, "text/html")
                email.send()
                return render(request, "login.html")
            else:
                return HttpResponse("Error sending email !!!")
        else:
            return HttpResponse("Your passwords mismatch")
    else:
        return render(request, "registration.html")

def contact(request):
    if request.method == 'POST':
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        message = request.POST.get("message")
        obj = contact_table.objects.create(name=name, email=email, phone=phone, message=message)
        obj.save()
        return HttpResponse("Thank you for your support. We'll get back to you as soon as possible.")
    else:
        return render(request, "contact.html")

def about(request):
    if request.method == 'POST':
        return HttpResponse("")
    else:
        return render(request, "about.html")

def index(request):
    if request.method == 'POST':
        return HttpResponse("")
    else:
        return render(request, "index.html")

def service(request):
    if request.method == 'POST':
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        vehicle = request.POST.get("vehicle")
        date = request.POST.get("date")
        time = request.POST.get("time")
        duration = request.POST.get("duration")
        loc = request.POST.get("loc")
        request.session['loc'] = loc
        obj = reservation.objects.create(name=name, email=email, phone=phone, vehicle=vehicle, date=date, time=time, duration=duration, loc=loc)
        obj.save()
        return HttpResponse("Successfully reserved for parking."
                            "Wait for the admin to confirm your reservation.")
    else:
        return render(request, "service.html")

def location(request):
    try:
        idukki = slots_table.objects.get(location='Idukki')
        trivandrum = slots_table.objects.get(location='Trivandrum')
        ernakulam = slots_table.objects.get(location='Ernakulam')
        chennai = slots_table.objects.get(location='Chennai')
    except Http404:
        return HttpResponse("No slots available for one or more locations")
    return render(request, "location.html", {
        'Idukki_Slots': idukki.available_slots,
        'Trivandrum_Slots': trivandrum.available_slots,
        'Ernakulam_Slots': ernakulam.available_slots,
        'Chennai_Slots': chennai.available_slots
    })

def faq(request):
    if request.method == 'POST':
        return HttpResponse("")
    else:
        return render(request, "faq.html")

def privacy_policy(request):
    if request.method == 'POST':
        return HttpResponse("")
    else:
        return render(request, "privacy_policy.html")

def terms_and_conditions(request):
    if request.method == 'POST':
        return HttpResponse("")
    else:
        return render(request, "terms_and_conditions.html")

def bookings(request):
    view_book = reservation.objects.all()
    return render(request, "admin/bookings.html", {'book': view_book})

def feedback(request):
    view_feeds = contact_table.objects.all()
    return render(request, "admin/feedback.html", {'feeds': view_feeds})

def delete_feedback(request, id):
    if request.method == 'POST':
        details = get_object_or_404(contact_table, id=id)
        details.delete()
    return redirect("feedback")

def view_locations(request):
    try:
        idukki = slots_table.objects.get(location='Idukki')
        trivandrum = slots_table.objects.get(location='Trivandrum')
        ernakulam = slots_table.objects.get(location='Ernakulam')
        chennai = slots_table.objects.get(location='Chennai')
    except Http404:
        return HttpResponse("No slots available for one or more locations")
    return render(request, "admin/view_locations.html", {
        'Idukki_Slots': idukki.available_slots,
        'Trivandrum_Slots': trivandrum.available_slots,
        'Ernakulam_Slots': ernakulam.available_slots,
        'Chennai_Slots': chennai.available_slots
    })

def booking_accept(request, id):
    if request.method == 'POST':
        details = get_object_or_404(reservation, id=id)
        details.flag = True
        details.save()
        email = request.POST.get("email")
        location = details.loc
        slot_details = get_object_or_404(slots_table, location=location)
        if slot_details.reserved_slots < slot_details.max_slots:
            slot_details.reserved_slots += 1
            slot_details.available_slots -= 1
            slot_details.save()
        else:
            return HttpResponse("No Available Slots")
        if details:
            details.save()
            html_message = render_to_string('email_accept.html', {'variable': 'value'})
            plain_text = strip_tags(html_message)
            email = EmailMultiAlternatives(
                subject='PARKER',
                body=plain_text,
                from_email='prasanthrajan1121@gmail.com',
                to=[email, "prasanthrajan1121@gmail.com"],
            )
            email.attach_alternative(html_message, "text/html")
            email.send()
            return render(request, "admin/bookings.html")
        else:
            return HttpResponse("Error sending email !!!")
    return redirect("bookings")

def booking_delete(request, id):
    if request.method == 'POST':
        details = get_object_or_404(reservation, id=id)
        details.delete()
        email = request.POST.get("email")
        if details:
            html_message = render_to_string('email_reject.html', {'variable': 'value'})
            plain_text = strip_tags(html_message)
            email = EmailMultiAlternatives(
                subject='PARKER',
                body=plain_text,
                from_email='prasanthrajan1121@gmail.com',
                to=[email, "prasanthrajan1121@gmail.com"],
            )
            email.attach_alternative(html_message, "text/html")
            email.send()
            return render(request, "admin/bookings.html")
        else:
            return HttpResponse("Error sending email !!!")
    return redirect("bookings")

def subscribe(request):
    if request.method == 'POST':
        email = request.POST.get("sub_email")
        subscriber, created = subscribers_table.objects.get_or_create(email=email)
        if subscriber.subscribe():
            return HttpResponse("Successfully Subscribed")
        else:
            return HttpResponse("Already Subscribed")
    return render(request, "index.html")

def delete_subscribers(request, id):
    if request.method == 'POST':
        sub = get_object_or_404(subscribers_table, id=id)
        sub.delete()
    return render(request, "admin/admin_index.html")

def vacate(request):
    if request.method == 'POST':
        email = request.session.get('email')
        location = request.session.get('loc')
        reservation_details = get_object_or_404(reservation, email=email)
        if reservation_details:
            slot_details = get_object_or_404(slots_table, location=location)
            if slot_details:
                slot_details.available_slots += 1
                slot_details.reserved_slots -= 1
                slot_details.save()
                reservation_details.delete()
                return redirect('user_exp')
            else:
                return HttpResponse("There is no location for the user")
        else:
            return HttpResponse("You are not reserved any parking slots.")
    return render(request, "service.html")
    
    return redirect('user_exp')

def user_exp(request):
    if request.method == 'POST':
        name = request.session.get('name')
        email = request.session.get('email')
        experience = request.POST.get('experience')
        rating = request.POST.get('rating')

        if experience and rating:
            try:
                rating = int(rating) 
                if 1 <= rating <= 5:
                    feedback = feedback_table.objects.create(name=name, email=email, experience=experience, rating=rating)
                    feedback.save()
                    return HttpResponse("Thank you for your feedback!")
                else:
                    return HttpResponse("Invalid rating value.")
            except ValueError:
                return HttpResponse("Invalid rating value.")
        else:
            return HttpResponse("Experience and rating are required.")

    return render(request, 'user_experience.html')

def view_user_experience(request):
    feedbacks = feedback_table.objects.all()
    return render(request, "admin/user_feedback.html", {'feedbacks': feedbacks})

def user_feedback(request):
    if request.method == 'POST':
        return HttpResponse("")
    else:
        return render(request, "admin/user_feedback.html")    

def delete_user_feedback(request, id):
    if request.method == 'POST':
        details = get_object_or_404(feedback_table, id=id)
        details.delete()
    return redirect("user_feedback")