from django.core.validators import MinLengthValidator, MaxLengthValidator
from django.db import models

# Create your models here.


class Register(models.Model):
    fname = models.CharField(max_length=1000, null=True)
    lname = models.CharField(max_length=1000, null=True)
    name = models.CharField(max_length=1000, null=True)
    email = models.CharField(max_length=1000, null=True)
    phno = models.IntegerField(max_length=10,null=True)
    password = models.CharField( max_length=100,  
        validators=[MinLengthValidator(2), MaxLengthValidator(100)] ,null=True)
    confirmpassword = models.CharField( max_length=100,  
        validators=[MinLengthValidator(2), MaxLengthValidator(100)] ,null=True)


    def __str__(self):
        return self.name


class Booking(models.Model):
    fname = models.CharField(max_length=1000, null=True)
    lname = models.CharField(max_length=1000, null=True)
    name = models.CharField(max_length=1000, null=True)
    email = models.CharField(max_length=1000, null=True)
    phno = models.IntegerField(max_length=10,null=True)
    servicedepartement = models.CharField(max_length=1000, null=True)
    sevicesub =models.CharField(max_length=1000, null=True)
    address = models.CharField(max_length=10000, null=True)

    def __str__(self):
        if self.name:
            return self.name
        return f"Booking {self.id}"


class Employee(models.Model):
    fname = models.CharField(max_length=1000, null=True)
    name = models.CharField(max_length=1000, null=True)
    email = models.CharField(max_length=1000, null=True)
    phno = models.IntegerField(max_length=10,null=True)
    sevicesub =models.CharField(max_length=1000, null=True)

    def __str__(self):
        if self.name:
            return self.name
        return f"Employee {self.id}"



from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=20)
    otp = models.CharField(max_length=4)
    is_verified = models.BooleanField(default=False)


class PhoneOTP(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15, unique=True)
    otp = models.CharField(max_length=6, default='')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
