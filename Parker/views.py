from django.shortcuts import render, HttpResponse, HttpResponseRedirect, reverse
from django.shortcuts import render, redirect, get_object_or_404
from django.db import models
# from Parker.ParkerApp.models import *
from ParkerApp.models import *
from django.http import HttpResponse, Http404


def user_login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        if email == 'admin@gmail.com' and password == 'admin':
            return redirect('admin_index')

        log = get_object_or_404(register_table, email=email)

        if email == log.email and password == log.password:
            request.session['name'] = log.name
            request.session['email'] = log.email
            # print(request.session.get('name'))
            return render(request, 'index.html')
        else:
            return HttpResponse("Your email and password didn't match")
    else:
        return render(request, "login.html")

def admin_index(request):
    try:
        sub = subscribers_table.objects.all()
        idukki = slots_table.objects.get(location='Idukki')
        trivandrum = slots_table.objects.get(location='Trivandrum')
        ernakulam = slots_table.objects.get(location='Ernakulam')
        chennai = slots_table.objects.get(location='Chennai')
    except Http404:
        return HttpResponse("No slots available for one or more locations")
    return render(request, "admin/admin_index.html", {
        'Idukki_Available': idukki.available_slots,
        'Idukki_Reserved': idukki.reserved_slots,
        'Idukki': idukki.location,
        'Trivandrum_Available': trivandrum.available_slots,
        'Trivandrum_Reserved': trivandrum.reserved_slots,
        'Trivandrum': trivandrum.location,
        'Ernakulam_Available': ernakulam.available_slots,
        'Ernakulam_Reserved': ernakulam.reserved_slots,
        'Ernakulam': ernakulam.location,
        'Chennai_Available': chennai.available_slots,
        'Chennai_Reserved': chennai.reserved_slots,
        'Chennai': chennai.location,
        'sub': sub
    })
