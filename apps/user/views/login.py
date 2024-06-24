# accounts/views.py

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views import View
from apps.user.forms import LoginForm


class LoginView(View):
    def get(self, request):
        form = LoginForm()
        return render(request, 'user/login.html', {'form': form})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                form.add_error(None, 'İstifadəçi adı və ya şifrə yanlışdır.')
        return render(request, 'user/login.html', {'form': form})
