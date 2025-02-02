# Generated by Django 5.1.5 on 2025-02-02 21:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_appointment_options_alter_appointment_car_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='status',
            field=models.CharField(choices=[('pending', 'Ожидает'), ('in_progress', 'В процессе'), ('completed', 'Выполнено'), ('canceled', 'Отменено')], default='pending', max_length=20, verbose_name='Статус заявки'),
        ),
    ]
