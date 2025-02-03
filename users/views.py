from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import RegistrationForm
from main.models import Appointment
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


# Регистрация пользователя
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = form.cleaned_data['phone']  # Используем телефон как логин
            user.first_name = form.cleaned_data['name']
            user.email = form.cleaned_data['email']     # ✅ Сохраняем почту
            user.save()

            # Привязка заявок по телефону
            appointments = Appointment.objects.filter(phone=user.phone)
            for appointment in appointments:
                appointment.user = user
                appointment.save()

            login(request, user)
            return redirect('dashboard')
        else:
            print("Ошибки формы:", form.errors)
    else:
        form = RegistrationForm()

    return render(request, 'main/register.html', {'form': form})


# Личный кабинет
@login_required  # ✅ Проверка авторизации
def dashboard(request):
    appointments = Appointment.objects.filter(user=request.user)
    return render(request, 'main/dashboard.html', {
        'user_name': request.user.first_name,
        'appointments': appointments
    })

# Вход в личный кабинет
def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')  # Телефон
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')  # Перенаправление в личный кабинет
        else:
            messages.error(request, 'Неверный телефон или пароль.')  # Ошибка авторизации

    return render(request, 'main/login.html')   # Шаблон login.html (если нужно)

# Выход из личного кабинета
def user_logout(request):
    logout(request)
    return redirect('index')