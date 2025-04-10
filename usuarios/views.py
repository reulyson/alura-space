from django.shortcuts import render
from .forms import LoginForm

def login(request): # Função para renderizar a página de login

    form = LoginForm()
    return render(request, 'usuarios/login.html', {'form': form})

def cadastro(request): # Função para renderizar a página de cadastro
    return render(request, 'usuarios/cadastro.html')
