from django.db import models
from django.contrib.auth.models import User

class register_table(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.email

class contact_table(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20)
    message = models.TextField()

    def __str__(self):
        return self.name

class reservation(models.Model):
    flag = models.BooleanField(default=False)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=10)
    vehicle = models.CharField(max_length=50)
    date = models.DateField()
    time = models.TimeField()
    duration = models.FloatField()
    options = (
        ('Idukki', 'Idukki'),
        ('Ernakulam', 'Ernakulam'),
        ('Trivandrum', 'Trivandrum'),
        ('Chennai', 'Chennai'),
    )
    loc = models.CharField(max_length=20, choices=options)

    def __str__(self):
        return self.vehicle
    
class slots_table(models.Model):
    location = models.CharField(unique=True, max_length=100)
    available_slots	= models.IntegerField()
    reserved_slots = models.IntegerField()
    max_slots = models.IntegerField(default=40)

    def __str__(self):
        return self.location

class subscribers_table(models.Model):
    email = models.EmailField(unique=True)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.email

    def subscribe(self):
        if not self.status:
            self.status = True
            self.save()
            return True
        else:
            return False

class feedback_table(models.Model):
    name = models.CharField(max_length=100, default='Name')
    email = models.EmailField(default='Email@gmail.com')
    experience = models.TextField()
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)])

    def __str__(self):
        return self.name