from django.db import models
from django.contrib.auth.models import User
import uuid

class Worker(models.Model):
  name = models.CharField(max_length=50)
  pin = models.CharField(max_length=6)
  mobile = models.CharField(max_length=10)
  work =  models.CharField(max_length=50)
  
  
def __str__(self):
    return f"{self.name} {self.pin} {self.mobile} {self.work}"

class Location(models.Model):
    name = models.CharField(max_length=100)
    place = models.CharField(max_length=100)
    contact = models.CharField(max_length=100)
    pin_codes = models.ManyToManyField('PinCode')
    services = models.ManyToManyField('Service')

    class Meta:
     verbose_name = 'Dealer' 

class PinCode(models.Model):
    code = models.CharField(max_length=10)
    def __str__(self):
        return self.code
class Service(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name
    


class Customer(models.Model):
    name = models.CharField(max_length=100)
    mobile = models.CharField(max_length=10)
    worker_name = models.CharField(max_length=255)
    worker_number = models.CharField(max_length=20)
    worker_work = models.CharField(max_length=255)
    date = models.DateTimeField(auto_now_add=True)
    email = models.EmailField(blank=True, null=True) 
    address_line_1 = models.CharField(max_length=255)
    address_line_2 = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=20)
    approved = models.BooleanField(default=False)

# Create your models here.
class Profile(models.Model):
    user=models.OneToOneField(User,   on_delete=models.CASCADE,related_name="profile")
    phone_number=models.CharField(max_length=15)
    otp=models.CharField(max_length=100,null=True,blank=True)
    pincode=models.CharField(max_length=8)
    bookings = models.ManyToManyField(Customer, blank=True, related_name="profiles")
    

    def __str__(self):
        return self.user.username