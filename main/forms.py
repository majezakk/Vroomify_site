from django import forms
from main.models import *

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['name', 'phone', 'car', 'service', 'date', 'time']