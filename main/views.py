from django.http import JsonResponse
from django.shortcuts import render, redirect
from main.forms import AppointmentForm

def index(request):
    return render(request, 'main/index.html')

def more_content(request):
    return render(request, 'main/more_content.html')

def register(request):
    return render(request, 'main/register.html')


def create_appointment(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({'success': True, 'message': 'Запись успешно создана!'})
        else:
            return JsonResponse({'success': False, 'errors': form.errors})

    return JsonResponse({'success': False, 'message': 'Неверный запрос'})