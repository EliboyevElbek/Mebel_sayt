from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms

from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('username', 'email', 'first_name', 'last_name', 'city', 'phone_num')
        # widgets = {
        #     'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Foydalanuvchi nomi'}),
        #     'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email manzilingiz'}),
        #     'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ismingiz'}),
        #     'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Familiyangiz'}),
        #     'city': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Shahringiz'}),
        #     'phone_num': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Telefon raqamingiz'}),
        #     'password1': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Parol'}),
        #     'password2': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Parolni takrorlang'}),
        # }
        # labels = {
        #     'username': 'Foydalanuvchi nomi',
        #     'email': 'Email manzil',
        #     'first_name': 'Ism',
        #     'last_name': 'Familiya',
        #     'city': 'Manzil',
        #     'phone_num': 'Telefon raqam',
        # }
        # help_texts = {
        #     'username': 'Foydalanuvchi nomi 150 ta belgidan kam bo\'lishi kerak.',
        #     'email': 'Email manzilingizni kiriting.',
        #     'first_name': 'Ismingizni kiriting.',
        #     'last_name': 'Familiyangizni kiriting.',
        #     'city': 'Iltimos, shahringizni kiriting.',
        #     'phone_num': 'Telefon raqamingizni kiriting (masalan: +998901234567).',
        # }


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'first_name', 'last_name', 'city', 'phone_num')