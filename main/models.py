from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _


class Appointment(models.Model):
    STATUS_CHOICES = [
        ('pending', _('Ожидает')),
        ('in_progress', _('В процессе')),
        ('completed', _('Выполнено')),
        ('canceled', _('Отменено')),
    ]

    SERVICE_CHOICES = [
        ('diagnostics', _('Диагностика автомобиля')),
        ('engine_repair', _('Ремонт двигателя и трансмиссии')),
        ('maintenance', _('Замена масла и техническое обслуживание')),
        ('body_repair', _('Кузовной ремонт и покраска')),
        ('tire_change', _('Замена шин и балансировка')),
        ('ac_service', _('Обслуживание кондиционера')),
    ]

    name = models.CharField(_('Имя клиента'), max_length=100)
    phone = models.CharField(_('Телефон'), max_length=20)
    car = models.CharField(_('Автомобиль'), max_length=100)
    service = models.CharField(_('Услуга'), max_length=20, choices=SERVICE_CHOICES)
    date = models.DateField(_('Дата'))
    time = models.TimeField(_('Время'))
    status = models.CharField(_('Статус заявки'), max_length=20, choices=STATUS_CHOICES, default='pending')  # Добавлено поле
    created_at = models.DateTimeField(_('Дата создания'), auto_now_add=True)
    last_modified = models.DateTimeField(_('Последнее изменение'), auto_now=True)

    class Meta:
        verbose_name = _('Запись на услугу')
        verbose_name_plural = _('Записи на услуги')

    def __str__(self):
        return f"{self.name} - {self.service} на {self.date} в {self.time} ({self.get_status_display()})"

from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

class StatusChangeLog(models.Model):
    appointment = models.ForeignKey(
        'Appointment',
        on_delete=models.CASCADE,
        related_name='status_changes',
        verbose_name=_('Заявка')
    )
    previous_status = models.CharField(
        _('Предыдущий статус'),
        max_length=20,
        choices=Appointment.STATUS_CHOICES
    )
    new_status = models.CharField(
        _('Новый статус'),
        max_length=20,
        choices=Appointment.STATUS_CHOICES
    )
    changed_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name=_('Изменил пользователь')
    )
    timestamp = models.DateTimeField(
        _('Дата изменения'),
        auto_now_add=True
    )

    class Meta:
        verbose_name = _('Изменение статуса')
        verbose_name_plural = _('История изменений статусов')
        ordering = ['-timestamp']  # Сортировка по дате изменения (сначала новые)

    def __str__(self):
        return f"{self.appointment} изменён с {self.get_previous_status_display()} на {self.get_new_status_display()}"
