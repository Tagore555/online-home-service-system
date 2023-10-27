from django.contrib import admin
from .models import Register,Booking,UserProfile,Employee
# Register your models here.
admin.site.register(Register)
admin.site.register(Booking)
admin.site.register(Employee)



admin.site.register(UserProfile)