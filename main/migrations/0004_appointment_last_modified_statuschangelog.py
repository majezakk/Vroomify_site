# Generated by Django 5.1.5 on 2025-02-02 22:31

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_appointment_status'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='last_modified',
            field=models.DateTimeField(auto_now=True, verbose_name='Последнее изменение'),
        ),
        migrations.CreateModel(
            name='StatusChangeLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('previous_status', models.CharField(choices=[('pending', 'Ожидает'), ('in_progress', 'В процессе'), ('completed', 'Выполнено'), ('canceled', 'Отменено')], max_length=20, verbose_name='Предыдущий статус')),
                ('new_status', models.CharField(choices=[('pending', 'Ожидает'), ('in_progress', 'В процессе'), ('completed', 'Выполнено'), ('canceled', 'Отменено')], max_length=20, verbose_name='Новый статус')),
                ('timestamp', models.DateTimeField(auto_now_add=True, verbose_name='Дата изменения')),
                ('appointment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='status_changes', to='main.appointment')),
                ('changed_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Изменил пользователь')),
            ],
        ),
    ]
