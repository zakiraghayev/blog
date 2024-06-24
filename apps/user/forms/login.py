# accounts/forms.py

from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(max_length=255, label='İstifadəçi adı')
    password = forms.CharField(widget=forms.PasswordInput, label='Şifrə')
