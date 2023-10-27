from django.forms import ModelForm
#from .models import Details

class RegisterForm(ModelForm):
    class Meta:
        model = Register
        fields = '__all__'



class BookingForm(ModelForm):
    class Meta:
        model = Booking
        fields = '__all__'


class EmployeeForm(ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'
