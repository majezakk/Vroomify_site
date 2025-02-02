from django.db import models
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

    class Meta:
        verbose_name = _('Запись на услугу')
        verbose_name_plural = _('Записи на услуги')

    def __str__(self):
        return f"{self.name} - {self.service} на {self.date} в {self.time} ({self.get_status_display()})"

