from django.shortcuts import render

def login(request): # Função para renderizar a página de login
    return render(request, 'usuarios/login.html')

def cadastro(request): # Função para renderizar a página de cadastro
    return render(request, 'usuarios/cadastro.html')
