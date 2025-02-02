from django.contrib import admin
from .models import Appointment, StatusChangeLog
from django.utils.html import format_html
from django.utils.translation import gettext_lazy as _

# Отображение истории изменений статуса
@admin.register(StatusChangeLog)
class StatusChangeLogAdmin(admin.ModelAdmin):
    list_display = ('appointment', 'previous_status_display', 'new_status_display', 'changed_by', 'timestamp')
    list_filter = ('new_status', 'changed_by')
    search_fields = ('appointment__name', 'changed_by__username')
    verbose_name = _('История изменений статусов')
    verbose_name_plural = _('История изменений статусов')

    # Локализация статусов
    def previous_status_display(self, obj):
        return dict(Appointment.STATUS_CHOICES).get(obj.previous_status, obj.previous_status)
    previous_status_display.short_description = _('Предыдущий статус')

    def new_status_display(self, obj):
        return dict(Appointment.STATUS_CHOICES).get(obj.new_status, obj.new_status)
    new_status_display.short_description = _('Новый статус')


# Встраивание истории изменений в заявку
class StatusChangeInline(admin.TabularInline):
    model = StatusChangeLog
    extra = 0
    readonly_fields = ('previous_status', 'new_status', 'changed_by', 'timestamp')
    can_delete = False
    verbose_name = _('История изменения статуса')
    verbose_name_plural = _('История изменений статусов')


@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'car', 'service_display', 'date', 'time', 'status_colored', 'created_at', 'last_modified')
    list_filter = ('service', 'date', 'status')
    search_fields = ('name', 'phone', 'car')
    inlines = [StatusChangeInline]  # Встраивание истории изменений в заявку

    # Локализация статусов
    def save_model(self, request, obj, form, change):
        if change:
            old_obj = Appointment.objects.get(pk=obj.pk)
            if old_obj.status != obj.status:
                StatusChangeLog.objects.create(
                    appointment=obj,
                    previous_status=old_obj.status,
                    new_status=obj.status,
                    changed_by=request.user
                )
        super().save_model(request, obj, form, change)

    def status_colored(self, obj):
        color_map = {
            'pending': 'orange',
            'in_progress': 'blue',
            'completed': 'green',
            'canceled': 'red',
        }
        return format_html(
            '<span style="color: {}; font-weight: bold;">{}</span>',
            color_map.get(obj.status, 'black'),
            obj.get_status_display()
        )

    status_colored.short_description = _('Статус')

    # Локализация услуги
    def service_display(self, obj):
        return dict(Appointment.SERVICE_CHOICES).get(obj.service, obj.service)
    service_display.short_description = _('Услуга')
