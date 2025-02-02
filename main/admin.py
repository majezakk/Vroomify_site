from django.contrib import admin
from .models import Appointment
from django.utils.translation import gettext_lazy as _

@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'car', 'service', 'date', 'time', 'status', 'created_at')
    list_filter = ('service', 'date', 'status')
    search_fields = ('name', 'phone', 'car')
