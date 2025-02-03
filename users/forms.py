from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class RegistrationForm(UserCreationForm):
    name = forms.CharField(max_length=100, label='Имя')
    phone = forms.CharField(max_length=15, label='Телефон')
    email = forms.EmailField(label='Почта')

    password1 = forms.CharField(  # ✅ Правильное поле для пароля
        label='Пароль',
        widget=forms.PasswordInput,
        strip=False,
        help_text='Введите пароль (не менее 8 символов).'
    )
    password2 = forms.CharField(  # ✅ Правильное поле для подтверждения пароля
        label='Подтверждение пароля',
        widget=forms.PasswordInput,
        strip=False,
        help_text='Повторите пароль для подтверждения.'
    )

    class Meta:
        model = CustomUser
        fields = ['name', 'phone', 'email', 'password1', 'password2']

    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        if CustomUser.objects.filter(phone=phone).exists():
            raise forms.ValidationError("Пользователь с таким номером телефона уже существует.")
        return phone
