from django.shortcuts import render, redirect
from .forms import LoginForm, CadastroForm

def login(request): # Função para renderizar a página de login

    form = LoginForm()
    return render(request, 'usuarios/login.html', {'form': form})

def cadastro(request): # Função para renderizar a página de cadastro

    form = CadastroForm()

    if request.method == 'POST': # Verifica se o método da requisição é POST
        form = CadastroForm(request.POST) # Cria um formulário com os dados da requisição
        if form['senha_1'].value() != form['senha_2'].value(): # Verifica se as senhas são iguais
            return redirect('cadastro')
        

    return render(request, 'usuarios/cadastro.html', {'form': form})
