from django.shortcuts import render
from .models import *
from django.shortcuts import get_object_or_404
from django.http import FileResponse
from django.shortcuts import redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.db.models import Q,F
from django.contrib.auth.forms import UserCreationForm
import random
from django.contrib.auth.decorators import login_required
import asynchat
from django.core.mail import send_mail
from django.core.mail import send_mass_mail
import smtplib
from django.core.exceptions import ValidationError


def loginPage(request):
   page ='login'

   if request.user.is_authenticated:
      return redirect('services')

   if request.method=='POST':
      username=request.POST.get('username').lower()
      password=request.POST.get('password')
      try:
         user =User.objects.get(username=username)
      except:
         messages.error(request,'User does not exits')

      user=authenticate(request,username=username,password=password)

      if user is not None:
         login(request,user)
         return redirect('services')
      else:
          messages.error(request,'Username or password does not exits')
   context={'page':page}
   return render(request,'base/login_register.html',context)

def logoutUser(request):
   logout(request)
   return redirect('home')

def employee(request):
   if request.method == 'POST':
         job=request.POST.get('job')
         fname= request.POST.get('fname')
         username = request.POST.get('username')
         email = request.POST.get('email')
         phno = request.POST.get('phno')
         password = request.POST.get('password')
         confirm_password = request.POST.get('confirm_password')
         if(job=="tv"):
            username="tv-"+username
         elif(job=="geyser"):
            username="geyser-"+username
         elif(job=="refrigiter"):
            username="refrigiter-"+username
         elif(job=="washing_machine"):
            username="washing_machine-"+username
         elif(job=="microwave_oven"):
            username="microwave_oven-"+username
         elif(job=="water_purifier"):
            username="water_purifier-"+username

         elif(job=="installation"):
            username="installation-"+username
         elif(job=="uninstallation"):
            username="uninstallation-"+username
         elif(job=="ac_reapir"):
            username="ac_reapir-"+username
         elif(job=="gas_refill"):
            username="gas_refill-"+username
         elif(job=="wet_servicing"):
            username="wet_servicing-"+username
         elif(job=="dry_servicing"):
            username="dry_servicing-"+username


         elif(job=="laundery"):
            username="laundery-"+username
         elif(job=="electrical"):
            username="electrical-"+username
         elif(job=="pest_control"):
            username="pest_control-"+username
         elif(job=="carpentry"):
            username="carpentry-"+username
         elif(job=="plumbing"):
            username="plumbing-"+username
         elif(job=="painnting"):
            username="painnting-"+username

         try:
               is_valid_password(password)

               if password == confirm_password:
                  if not User.objects.filter(username=username).exists():
                     user = User.objects.create_user(username=username, password=password)
                     messages.success(request, 'Registration successful. You can now log in.')
                     emp=Employee()
                     emp.fname=fname
                     emp.name=username
                     emp.email=email
                     emp.phno=phno
                     if(job=="tv"):
                        emp.sevicesub="tv"
                     elif(job=="geyser"):
                        emp.sevicesub="geyser"
                     elif(job=="refrigiter"):
                        emp.sevicesub="refrigiter"
                     elif(job=="washing_machine"):
                        emp.sevicesub="washing_machine"
                     elif(job=="microwave_oven"):
                        emp.sevicesub="microwave_oven"
                     elif(job=="water_purifier"):
                        emp.sevicesub="water_purifier"

                     elif(job=="installation"):
                        emp.sevicesub="installation"
                     elif(job=="uninstallation"):
                        emp.sevicesub="uninstallation"
                     elif(job=="ac_reapir"):
                        emp.sevicesub="ac_reapir"
                     elif(job=="gas_refill"):
                        emp.sevicesub="gas_refill"
                     elif(job=="wet_servicing"):
                        emp.sevicesub="wet_servicing"
                     elif(job=="dry_servicing"):
                        emp.sevicesub="dry_servicing"


                     elif(job=="laundery"):
                        emp.sevicesub="laundery"
                     elif(job=="electrical"):
                        emp.sevicesub="electrical"
                     elif(job=="pest_control"):
                        emp.sevicesub="pest_control"
                     elif(job=="carpentry"):
                        emp.sevicesub="carpentry"
                     elif(job=="plumbing"):
                        emp.sevicesub="plumbing"
                     elif(job=="painnting"):
                        emp.sevicesub="painnting"
                     emp.save()
                     a=("Username: "+username+"\n"+"Password: "+password)
                     if email:
                        try:
                           send_mail(
                              'Your Selected',
                              a,
                              'onlinehomeservices117@gmail.com',
                              [email],
                              fail_silently=False,
                           )
                        except smtplib.SMTPAuthenticationError:
                           print('The username and password are not accepted.')
                        except Exception as e:
                           print('An error occurred while sending email: '+str(e))
                        else:
                           print('Email sent successfully.')
                     return redirect('login')
                  else:
                     messages.error(request, 'An error occurred during registration. The username is already taken.')
               else:
                  messages.error(request, 'Passwords do not match. Please try again.')

         except ValidationError as e:
               messages.error(request, e)
   return render(request,'base/employee.html')

def is_valid_password(password):
    # Implement your custom password validation logic here
    if len(password) < 8:
        raise ValidationError("Password must be at least 8 characters long.")
    if not any(char.isdigit() for char in password):
        raise ValidationError("Password must contain at least one digit.")

def registerPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        try:
            is_valid_password(password)

            if password == confirm_password:
                if not User.objects.filter(username=username).exists():
                    user = User.objects.create_user(username=username, password=password)
                    messages.success(request, 'Registration successful. You can now log in.')
                    return redirect('login')
                else:
                    messages.error(request, 'An error occurred during registration. The username is already taken.')
            else:
                messages.error(request, 'Passwords do not match. Please try again.')

        except ValidationError as e:
            messages.error(request, e)
    return render(request,'base/login_register.html')

@login_required(login_url='login')
def services(request):
   application=request.POST.get('application')
   ac=request.POST.get('ac')
   homeneeds=request.POST.get('homeneeds')


   tv=request.POST.get('tv')
   geyser=request.POST.get('geyser')
   refrigiter=request.POST.get('refrigiter')
   washing_machine=request.POST.get('washing_machine')
   microwave_oven=request.POST.get('microwave_oven')
   water_purifier=request.POST.get('water_purifier')



   installation=request.POST.get('installation')
   uninstallation=request.POST.get('uninstallation')
   ac_reapir=request.POST.get('ac_reapir')
   gas_refill=request.POST.get('gas_refill')
   wet_servicing=request.POST.get('wet_servicing')
   dry_servicing=request.POST.get('dry_servicing')





   laundery=request.POST.get('laundery')
   electrical=request.POST.get('electrical')
   pest_control=request.POST.get('pest_control')
   carpentry=request.POST.get('carpentry')
   plumbing=request.POST.get('plumbing')
   painnting=request.POST.get('painnting')
   

   tv_book =request.POST.get('tv_booknow')
   geyser_book =request.POST.get('geyser_booknow')
   refrigiter_book =request.POST.get('refrigiter_booknow')
   washing_machine_book =request.POST.get('washing_machine_booknow')
   microwave_oven_book =request.POST.get('microwave_oven_booknow')
   water_purifier_book =request.POST.get('water_purifier_booknow')




   installation_book =request.POST.get('installation_booknow')
   uninstallation_book =request.POST.get('uninstallation_booknow')
   ac_reapir_book =request.POST.get('ac_reapir_booknow')
   gas_refill_book =request.POST.get('gas_refill_booknow')
   wet_servicing_book =request.POST.get('wet_servicing_booknow')
   dry_servicing_book =request.POST.get('dry_servicing_booknow')



   laundery_book =request.POST.get('laundery_booknow')
   electrical_book =request.POST.get('electrical_booknow')
   pest_control_book =request.POST.get('pest_control_booknow')
   carpentry_book =request.POST.get('carpentry_booknow')
   plumbing_book =request.POST.get('plumbing_booknow')
   painnting_book =request.POST.get('painnting_booknow')









   fname1 = request.POST.get('fname')
   lname1 = request.POST.get('lname')
   name1 = request.POST.get('name')
   email1 = request.POST.get('email')
   phno1 = request.POST.get('phno')
   address1 = request.POST.get('address')




   if request.method == 'POST':
      if (fname1 and lname1 and name1 and email1 and phno1 and address1 and tv_book):
         post=Booking()
         post.fname=fname1
         post.lname=lname1
         post.name=name1
         post.email=email1
         post.phno=phno1
         post.servicedepartement="application"
         post.sevicesub="tv"
         post.address=address1
         post.save()
         name_to_match = "tv"
         email_ids = Employee.objects.filter(sevicesub=name_to_match).values_list('email', flat=True)
         e=list(email_ids)
         f = random.choice(e)
         a=('Name:'+fname1+" "+lname1+"\n"+'Email: '+email1+"\n"+'Phone Number: '+phno1+"\n"+"Address: "+address1)
         print(a)
         if email1:
            try:
               message1 = (
                  "Your Work Mail",
                  a,
                  "onlinehomeservices117@gmail.com",
                  [f],
               )
               message2 = (
                  "Confermation mail from Online Home Service System",
                  "Ur order succssfully taken",
                  "onlinehomeservices117@gmail.com",
                  [email1],
               )
               send_mass_mail((message1, message2), fail_silently=False)
            except smtplib.SMTPAuthenticationError:
               print('The username and password are not accepted.')
            except Exception as e:
               print('An error occurred while sending email: '+str(e))
            else:
               print('Email sent successfully.')
         return HttpResponse("Thanks for the booking., You can get a confermation mail from us😊")
   if request.method == 'POST':
      if (fname1 and lname1 and name1 and email1 and phno1 and address1 and geyser_book):
         post=Booking()
         post.fname=fname1
         post.lname=lname1
         post.name=name1
         post.email=email1
         post.phno=phno1
         post.servicedepartement="application"
         post.sevicesub="geyser"
         post.address=address1
         post.save()
         name_to_match = "geyser"
         email_ids = Employee.objects.filter(sevicesub=name_to_match).values_list('email', flat=True)
         e=list(email_ids)
         f = random.choice(e)
         a=('Name:'+fname1+" "+lname1+"\n"+'Email: '+email1+"\n"+'Phone Number: '+phno1+"\n"+"Address: "+address1)
         print(a)
         if email1:
            try:
               message1 = (
                  "Your Work Mail",
                  a,
                  "onlinehomeservices117@gmail.com",
                  [f],
               )
               message2 = (
                  "Confermation Mail  from Online Home Service System",
                  "Ur order succssfully taken",
                  "onlinehomeservices117@gmail.com",
                  [email1],
               )
               send_mass_mail((message1, message2), fail_silently=False)
            except smtplib.SMTPAuthenticationError:
               print('The username and password are not accepted.')
            except Exception as e:
               print('An error occurred while sending email: '+str(e))
            else:
               print('Email sent successfully.')
         return HttpResponse("Thanks for the booking., You can get a confermation mail from us😊")
   if request.method == 'POST':
      if (fname1 and lname1 and name1 and email1 and phno1 and address1 and refrigiter_book):
         post=Booking()
         post.fname=fname1
         post.lname=lname1
         post.name=name1
         post.email=email1
         post.phno=phno1
         post.servicedepartement="application"
         post.sevicesub="refrigiter"
         post.address=address1
         post.save()
         name_to_match = "refrigiter"
         email_ids = Employee.objects.filter(sevicesub=name_to_match).values_list('email', flat=True)
         e=list(email_ids)
         f = random.choice(e)
         a=('Name:'+fname1+" "+lname1+"\n"+'Email: '+email1+"\n"+'Phone Number: '+phno1+"\n"+"Address: "+address1)
         print(a)
         if email1:
            try:
               message1 = (
                  "Your Work Mail",
                  a,
                  "onlinehomeservices117@gmail.com",
                  [f],
               )
               message2 = (
                  "Confermation mail from Online Home Service System",
                  "Ur order succssfully taken",
                  "onlinehomeservices117@gmail.com",
                  [email1],
               )
               send_mass_mail((message1, message2), fail_silently=False)
            except smtplib.SMTPAuthenticationError:
               print('The username and password are not accepted.')
            except Exception as e:
               print('An error occurred while sending email: '+str(e))
            else:
               print('Email sent successfully.')
         return HttpResponse("Thanks for the booking., You can get a confermation mail from us😊")
   if request.method == 'POST':
      if (fname1 and lname1 and name1 and email1 and phno1 and address1 and washing_machine_book):
         post=Booking()
         post.fname=fname1
         post.lname=lname1
         post.name=name1
         post.email=email1
         post.phno=phno1
         post.servicedepartement="application"
         post.sevicesub="washing_machine"
         post.address=address1
         post.save()
         name_to_match = "washing_machine"
         email_ids = Employee.objects.filter(sevicesub=name_to_match).values_list('email', flat=True)
         e=list(email_ids)
         f = random.choice(e)
         a=('Name:'+fname1+" "+lname1+"\n"+'Email: '+email1+"\n"+'Phone Number: '+phno1+"\n"+"Address: "+address1)
         print(a)
         if email1:
            try:
               message1 = (
                  "Your Work Mail",
                  a,
                  "onlinehomeservices117@gmail.com",
                  [f],
               )
               message2 = (
                  "Confermation Mail  from Online Home Service System",
                  "Ur order succssfully taken",
                  "onlinehomeservices117@gmail.com",
                  [email1],
               )
               send_mass_mail((message1, message2), fail_silently=False)
            except smtplib.SMTPAuthenticationError:
               print('The username and password are not accepted.')
            except Exception as e:
               print('An error occurred while sending email: '+str(e))
            else:
               print('Email sent successfully.')
         return HttpResponse("Thanks for the booking., You can get a confermation mail from us😊")
   if request.method == 'POST':
      if (fname1 and lname1 and name1 and email1 and phno1 and address1 and microwave_oven_book):
         post=Booking()
         post.fname=fname1
         post.lname=lname1
         post.name=name1
         post.email=email1
         post.phno=phno1
         post.servicedepartement="application"
         post.sevicesub="microwave_oven"
         post.address=address1
         post.save()
         name_to_match = "microwave_oven"
         email_ids = Employee.objects.filter(sevicesub=name_to_match).values_list('email', flat=True)
         e=list(email_ids)
         f = random.choice(e)
         a=('Name:'+fname1+" "+lname1+"\n"+'Email: '+email1+"\n"+'Phone Number: '+phno1+"\n"+"Address: "+address1)
         print(a)
         if email1:
            try:
               message1 = (
                  "Your Work Mail",
                  a,
                  "onlinehomeservices117@gmail.com",
                  [f],
               )
               message2 = (
                  "Confermation Mail  from Online Home Service System",
                  "Ur order succssfully taken",
                  "onlinehomeservices117@gmail.com",
                  [email1],
               )
               send_mass_mail((message1, message2), fail_silently=False)
            except smtplib.SMTPAuthenticationError:
               print('The username and password are not accepted.')
            except Exception as e:
               print('An error occurred while sending email: '+str(e))
            else:
               print('Email sent successfully.')
         return HttpResponse("Thanks for the booking., You can get a confermation mail from us😊")
   if request.method == 'POST':
      if (fname1 and lname1 and name1 and email1 and phno1 and address1 and water_purifier_book):
         post=Booking()
         post.fname=fname1
         post.lname=lname1
         post.name=name1
         post.email=email1
         post.phno=phno1
         post.servicedepartement="application"
         post.sevicesub="water_purifier"
         post.address=address1
         post.save()
         name_to_match = "water_purifier"
         email_ids = Employee.objects.filter(sevicesub=name_to_match).values_list('email', flat=True)
         e=list(email_ids)
         f = random.choice(e)
         a=('Name:'+fname1+" "+lname1+"\n"+'Email: '+email1+"\n"+'Phone Number: '+phno1+"\n"+"Address: "+address1)
         print(a)
         if email1:
            try:
               message1 = (
                  "Your Work Mail",
                  a,
                  "onlinehomeservices117@gmail.com",
                  [f],
               )
               message2 = (
                  "Confermation Mail  from Online Home Service System",
                  "Ur order succssfully taken",
                  "onlinehomeservices117@gmail.com",
                  [email1],
               )
               send_mass_mail((message1, message2), fail_silently=False)
            except smtplib.SMTPAuthenticationError:
               print('The username and password are not accepted.')
            except Exception as e:
               print('An error occurred while sending email: '+str(e))
            else:
               print('Email sent successfully.')
         return HttpResponse("Thanks for the booking., You can get a confermation mail from us😊")








   if request.method == 'POST':
      if (fname1 and lname1 and name1 and email1 and phno1 and address1 and installation_book):
         post=Booking()
         post.fname=fname1
         post.lname=lname1
         post.name=name1
         post.email=email1
         post.phno=phno1
         post.servicedepartement="ac"
         post.sevicesub="installation"
         post.address=address1
         post.save()
         name_to_match = "installation"
         email_ids = Employee.objects.filter(sevicesub=name_to_match).values_list('email', flat=True)
         e=list(email_ids)
         f = random.choice(e)
         a=('Name:'+fname1+" "+lname1+"\n"+'Email: '+email1+"\n"+'Phone Number: '+phno1+"\n"+"Address: "+address1)
         print(a)
         if email1:
            try:
               message1 = (
                  "Your Work Mail",
                  a,
                  "onlinehomeservices117@gmail.com",
                  [f],
               )
               message2 = (
                  "Confermation Mail  from Online Home Service System",
                  "Ur order succssfully taken",
                  "onlinehomeservices117@gmail.com",
                  [email1],
               )
               send_mass_mail((message1, message2), fail_silently=False)
            except smtplib.SMTPAuthenticationError:
               print('The username and password are not accepted.')
            except Exception as e:
               print('An error occurred while sending email: '+str(e))
            else:
               print('Email sent successfully.')
         return HttpResponse("Thanks for the booking., You can get a confermation mail from us😊")
   if request.method == 'POST':
      if (fname1 and lname1 and name1 and email1 and phno1 and address1 and uninstallation_book):
         post=Booking()
         post.fname=fname1
         post.lname=lname1
         post.name=name1
         post.email=email1
         post.phno=phno1
         post.servicedepartement="ac"
         post.sevicesub="uninstallation"
         post.address=address1
         post.save()
         name_to_match = "uninstallation"
         email_ids = Employee.objects.filter(sevicesub=name_to_match).values_list('email', flat=True)
         e=list(email_ids)
         f = random.choice(e)
         a=('Name:'+fname1+" "+lname1+"\n"+'Email: '+email1+"\n"+'Phone Number: '+phno1+"\n"+"Address: "+address1)
         print(a)
         if email1:
            try:
               message1 = (
                  "Your Work Mail",
                  a,
                  "onlinehomeservices117@gmail.com",
                  [f],
               )
               message2 = (
                  "Confermation Mail  from Online Home Service System",
                  "Ur order succssfully taken",
                  "onlinehomeservices117@gmail.com",
                  [email1],
               )
               send_mass_mail((message1, message2), fail_silently=False)
            except smtplib.SMTPAuthenticationError:
               print('The username and password are not accepted.')
            except Exception as e:
               print('An error occurred while sending email: '+str(e))
            else:
               print('Email sent successfully.')
         return HttpResponse("Thanks for the booking., You can get a confermation mail from us😊")
   if request.method == 'POST':
      if (fname1 and lname1 and name1 and email1 and phno1 and address1 and ac_reapir_book):
         post=Booking()
         post.fname=fname1
         post.lname=lname1
         post.name=name1
         post.email=email1
         post.phno=phno1
         post.servicedepartement="ac"
         post.sevicesub="ac_reapir"
         post.address=address1
         post.save()
         name_to_match = "ac_reapir"
         email_ids = Employee.objects.filter(sevicesub=name_to_match).values_list('email', flat=True)
         e=list(email_ids)
         f = random.choice(e)
         a=('Name:'+fname1+" "+lname1+"\n"+'Email: '+email1+"\n"+'Phone Number: '+phno1+"\n"+"Address: "+address1)
         print(a)
         if email1:
            try:
               message1 = (
                  "Your Work Mail",
                  a,
                  "onlinehomeservices117@gmail.com",
                  [f],
               )
               message2 = (
                  "Confermation Mail  from Online Home Service System",
                  "Ur order succssfully taken",
                  "onlinehomeservices117@gmail.com",
                  [email1],
               )
               send_mass_mail((message1, message2), fail_silently=False)
            except smtplib.SMTPAuthenticationError:
               print('The username and password are not accepted.')
            except Exception as e:
               print('An error occurred while sending email: '+str(e))
            else:
               print('Email sent successfully.')
         return HttpResponse("Thanks for the booking., You can get a confermation mail from us😊")
   if request.method == 'POST':
      if (fname1 and lname1 and name1 and email1 and phno1 and address1 and gas_refill_book):
         post=Booking()
         post.fname=fname1
         post.lname=lname1
         post.name=name1
         post.email=email1
         post.phno=phno1
         post.servicedepartement="ac"
         post.sevicesub="gas_refill"
         post.address=address1
         post.save()
         name_to_match = "gas_refill"
         email_ids = Employee.objects.filter(sevicesub=name_to_match).values_list('email', flat=True)
         e=list(email_ids)
         f = random.choice(e)
         a=('Name:'+fname1+" "+lname1+"\n"+'Email: '+email1+"\n"+'Phone Number: '+phno1+"\n"+"Address: "+address1)
         print(a)
         if email1:
            try:
               message1 = (
                  "Your Work Mail",
                  a,
                  "onlinehomeservices117@gmail.com",
                  [f],
               )
               message2 = (
                  "Confermation Mail  from Online Home Service System",
                  "Ur order succssfully taken",
                  "onlinehomeservices117@gmail.com",
                  [email1],
               )
               send_mass_mail((message1, message2), fail_silently=False)
            except smtplib.SMTPAuthenticationError:
               print('The username and password are not accepted.')
            except Exception as e:
               print('An error occurred while sending email: '+str(e))
            else:
               print('Email sent successfully.')
         return HttpResponse("Thanks for the booking., You can get a confermation mail from us😊")
   if request.method == 'POST':
      if (fname1 and lname1 and name1 and email1 and phno1 and address1 and wet_servicing_book):
         post=Booking()
         post.fname=fname1
         post.lname=lname1
         post.name=name1
         post.email=email1
         post.phno=phno1
         post.servicedepartement="ac"
         post.sevicesub="wet_servicing"
         post.address=address1
         post.save()
         name_to_match = "wet_servicing"
         email_ids = Employee.objects.filter(sevicesub=name_to_match).values_list('email', flat=True)
         e=list(email_ids)
         f = random.choice(e)
         a=('Name:'+fname1+" "+lname1+"\n"+'Email: '+email1+"\n"+'Phone Number: '+phno1+"\n"+"Address: "+address1)
         print(a)
         if email1:
            try:
               message1 = (
                  "Your Work Mail",
                  a,
                  "onlinehomeservices117@gmail.com",
                  [f],
               )
               message2 = (
                  "Confermation Mail  from Online Home Service System",
                  "Ur order succssfully taken",
                  "onlinehomeservices117@gmail.com",
                  [email1],
               )
               send_mass_mail((message1, message2), fail_silently=False)
            except smtplib.SMTPAuthenticationError:
               print('The username and password are not accepted.')
            except Exception as e:
               print('An error occurred while sending email: '+str(e))
            else:
               print('Email sent successfully.')
         return HttpResponse("Thanks for the booking., You can get a confermation mail from us😊")
   if request.method == 'POST':
      if (fname1 and lname1 and name1 and email1 and phno1 and address1 and dry_servicing_book):
         post=Booking()
         post.fname=fname1
         post.lname=lname1
         post.name=name1
         post.email=email1
         post.phno=phno1
         post.servicedepartement="ac"
         post.sevicesub="dry_servicing"
         post.address=address1
         post.save()
         name_to_match = "dry_servicing"
         email_ids = Employee.objects.filter(sevicesub=name_to_match).values_list('email', flat=True)
         e=list(email_ids)
         f = random.choice(e)
         a=('Name:'+fname1+" "+lname1+"\n"+'Email: '+email1+"\n"+'Phone Number: '+phno1+"\n"+"Address: "+address1)
         print(a)
         if email1:
            try:
               message1 = (
                  "Your Work Mail",
                  a,
                  "onlinehomeservices117@gmail.com",
                  [f],
               )
               message2 = (
                  "Confermation Mail  from Online Home Service System",
                  "Ur order succssfully taken",
                  "onlinehomeservices117@gmail.com",
                  [email1],
               )
               send_mass_mail((message1, message2), fail_silently=False)
            except smtplib.SMTPAuthenticationError:
               print('The username and password are not accepted.')
            except Exception as e:
               print('An error occurred while sending email: '+str(e))
            else:
               print('Email sent successfully.')
         return HttpResponse("Thanks for the booking., You can get a confermation mail from us😊")








   if request.method == 'POST':
      if (fname1 and lname1 and name1 and email1 and phno1 and address1 and laundery_book):
         post=Booking()
         post.fname=fname1
         post.lname=lname1
         post.name=name1
         post.email=email1
         post.phno=phno1
         post.servicedepartement="homeneeds"
         post.sevicesub="laundery"
         post.address=address1
         post.save()
         name_to_match = "laundery"
         email_ids = Employee.objects.filter(sevicesub=name_to_match).values_list('email', flat=True)
         e=list(email_ids)
         f = random.choice(e)
         a=('Name:'+fname1+" "+lname1+"\n"+'Email: '+email1+"\n"+'Phone Number: '+phno1+"\n"+"Address: "+address1)
         print(a)
         if email1:
            try:
               message1 = (
                  "Your Work Mail",
                  a,
                  "onlinehomeservices117@gmail.com",
                  [f],
               )
               message2 = (
                  "Confermation Mail  from Online Home Service System",
                  "Ur order succssfully taken",
                  "onlinehomeservices117@gmail.com",
                  [email1],
               )
               send_mass_mail((message1, message2), fail_silently=False)
            except smtplib.SMTPAuthenticationError:
               print('The username and password are not accepted.')
            except Exception as e:
               print('An error occurred while sending email: '+str(e))
            else:
               print('Email sent successfully.')
         return HttpResponse("Thanks for the booking., You can get a confermation mail from us😊")
   if request.method == 'POST':
      if (fname1 and lname1 and name1 and email1 and phno1 and address1 and electrical_book):
         post=Booking()
         post.fname=fname1
         post.lname=lname1
         post.name=name1
         post.email=email1
         post.phno=phno1
         post.servicedepartement="homeneeds"
         post.sevicesub="electrical"
         post.address=address1
         post.save()
         name_to_match = "electrical"
         email_ids = Employee.objects.filter(sevicesub=name_to_match).values_list('email', flat=True)
         e=list(email_ids)
         f = random.choice(e)
         a=('Name:'+fname1+" "+lname1+"\n"+'Email: '+email1+"\n"+'Phone Number: '+phno1+"\n"+"Address: "+address1)
         print(a)
         if email1:
            try:
               message1 = (
                  "Your Work Mail",
                  a,
                  "onlinehomeservices117@gmail.com",
                  [f],
               )
               message2 = (
                  "Confermation Mail  from Online Home Service System",
                  "Ur order succssfully taken",
                  "onlinehomeservices117@gmail.com",
                  [email1],
               )
               send_mass_mail((message1, message2), fail_silently=False)
            except smtplib.SMTPAuthenticationError:
               print('The username and password are not accepted.')
            except Exception as e:
               print('An error occurred while sending email: '+str(e))
            else:
               print('Email sent successfully.')
         return HttpResponse("Thanks for the booking., You can get a confermation mail from us😊")
   if request.method == 'POST':
      if (fname1 and lname1 and name1 and email1 and phno1 and address1 and pest_control_book):
         post=Booking()
         post.fname=fname1
         post.lname=lname1
         post.name=name1
         post.email=email1
         post.phno=phno1
         post.servicedepartement="homeneeds"
         post.sevicesub="pest_control"
         post.address=address1
         post.save()
         name_to_match = "pest_control"
         email_ids = Employee.objects.filter(sevicesub=name_to_match).values_list('email', flat=True)
         e=list(email_ids)
         f = random.choice(e)
         a=('Name:'+fname1+" "+lname1+"\n"+'Email: '+email1+"\n"+'Phone Number: '+phno1+"\n"+"Address: "+address1)
         print(a)
         if email1:
            try:
               message1 = (
                  "Your Work Mail",
                  a,
                  "onlinehomeservices117@gmail.com",
                  [f],
               )
               message2 = (
                  "Confermation Mail  from Online Home Service System",
                  "Ur order succssfully taken",
                  "onlinehomeservices117@gmail.com",
                  [email1],
               )
               send_mass_mail((message1, message2), fail_silently=False)
            except smtplib.SMTPAuthenticationError:
               print('The username and password are not accepted.')
            except Exception as e:
               print('An error occurred while sending email: '+str(e))
            else:
               print('Email sent successfully.')
         return HttpResponse("Thanks for the booking., You can get a confermation mail from us😊")
   if request.method == 'POST':
      if (fname1 and lname1 and name1 and email1 and phno1 and address1 and carpentry_book):
         post=Booking()
         post.fname=fname1
         post.lname=lname1
         post.name=name1
         post.email=email1
         post.phno=phno1
         post.servicedepartement="homeneeds"
         post.sevicesub="carpentry"
         post.address=address1
         post.save()
         name_to_match = "carpentry"
         email_ids = Employee.objects.filter(sevicesub=name_to_match).values_list('email', flat=True)
         e=list(email_ids)
         f = random.choice(e)
         a=('Name:'+fname1+" "+lname1+"\n"+'Email: '+email1+"\n"+'Phone Number: '+phno1+"\n"+"Address: "+address1)
         print(a)
         if email1:
            try:
               message1 = (
                  "Your Work Mail",
                  a,
                  "onlinehomeservices117@gmail.com",
                  [f],
               )
               message2 = (
                  "Confermation Mail  from Online Home Service System",
                  "Ur order succssfully taken",
                  "onlinehomeservices117@gmail.com",
                  [email1],
               )
               send_mass_mail((message1, message2), fail_silently=False)
            except smtplib.SMTPAuthenticationError:
               print('The username and password are not accepted.')
            except Exception as e:
               print('An error occurred while sending email: '+str(e))
            else:
               print('Email sent successfully.')
         return HttpResponse("Thanks for the booking., You can get a confermation mail from us😊")
   if request.method == 'POST':
      if (fname1 and lname1 and name1 and email1 and phno1 and address1 and plumbing_book):
         post=Booking()
         post.fname=fname1
         post.lname=lname1
         post.name=name1
         post.email=email1
         post.phno=phno1
         post.servicedepartement="homeneeds"
         post.sevicesub="plumbing"
         post.address=address1
         post.save()
         name_to_match = "plumbing"
         email_ids = Employee.objects.filter(sevicesub=name_to_match).values_list('email', flat=True)
         e=list(email_ids)
         f = random.choice(e)
         a=('Name:'+fname1+" "+lname1+"\n"+'Email: '+email1+"\n"+'Phone Number: '+phno1+"\n"+"Address: "+address1)
         print(a)
         if email1:
            try:
               message1 = (
                  "Your Work Mail",
                  a,
                  "onlinehomeservices117@gmail.com",
                  [f],
               )
               message2 = (
                  "Confermation Mail  from Online Home Service System",
                  "Ur order succssfully taken",
                  "onlinehomeservices117@gmail.com",
                  [email1],
               )
               send_mass_mail((message1, message2), fail_silently=False)
            except smtplib.SMTPAuthenticationError:
               print('The username and password are not accepted.')
            except Exception as e:
               print('An error occurred while sending email: '+str(e))
            else:
               print('Email sent successfully.')
         return HttpResponse("Thanks for the booking., You can get a confermation mail from us😊")
   if request.method == 'POST':
      if (fname1 and lname1 and name1 and email1 and phno1 and address1 and painnting_book):
         post=Booking()
         post.fname=fname1
         post.lname=lname1
         post.name=name1
         post.email=email1
         post.phno=phno1
         post.servicedepartement="homeneeds"
         post.sevicesub="painnting"
         post.address=address1
         post.save()
         name_to_match = "painnting"
         email_ids = Employee.objects.filter(sevicesub=name_to_match).values_list('email', flat=True)
         e=list(email_ids)
         f = random.choice(e)
         a=('Name:'+fname1+" "+lname1+"\n"+'Email: '+email1+"\n"+'Phone Number: '+phno1+"\n"+"Address: "+address1)
         print(a)
         if email1:
            try:
               message1 = (
                  "Your Work Mail",
                  a,
                  "onlinehomeservices117@gmail.com",
                  [f],
               )
               message2 = (
                  "Confermation Mail  from Online Home Service System",
                  "Ur order succssfully taken",
                  "onlinehomeservices117@gmail.com",
                  [email1],
               )
               send_mass_mail((message1, message2), fail_silently=False)
            except smtplib.SMTPAuthenticationError:
               print('The username and password are not accepted.')
            except Exception as e:
               print('An error occurred while sending email: '+str(e))
            else:
               print('Email sent successfully.')
         return HttpResponse("Thanks for the booking., You can get a confermation mail from us😊")









   
   
   
         
   
   context={'application':application,'ac':ac,'homeneeds':homeneeds,
            'tv':tv,'geyser':geyser,'refrigiter':refrigiter,'washing_machine':washing_machine,'microwave_oven':microwave_oven,'water_purifier':water_purifier,
            'installation':installation,'uninstallation':uninstallation,'ac_reapir':ac_reapir,'gas_refill':gas_refill,'wet_servicing':wet_servicing,'dry_servicing':dry_servicing,
            'laundery':laundery,'electrical':electrical,'pest_control':pest_control,'carpentry':carpentry,'plumbing':plumbing,'painnting':painnting}
   return render(request,'base/services.html',context)

def home(request):
    return render(request,'base/home.html')


def feedback(request):
   return render(request,'base/feedback.html')