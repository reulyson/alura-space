from django.shortcuts import render, redirect # Importa as funções render e redirect
from django.contrib.auth.models import User # Importa o modelo User
from .forms import LoginForm, CadastroForm # Importa os formulários

def login(request): # Função para renderizar a página de login

    form = LoginForm()
    return render(request, 'usuarios/login.html', {'form': form})

def cadastro(request): # Função para renderizar a página de cadastro

    form = CadastroForm()


    if request.method == 'POST': 
        form = CadastroForm(request.POST) # Cria um formulário com os dados da requisição
        
        # Verifica se o formulário é válido
        if form.is_valid(): 
            if form['senha_1'].value() != form['senha_2'].value(): # Verifica se as senhas são iguais
                return redirect('cadastro') # Redireciona para a página de cadastro
            
            # Armazena os dados do formulário
            primeiro = form['primeiro_nome'].value()
            ultimo = form['ultimo_nome'].value()
            nome = form['nome_cadastro'].value()
            email = form['email'].value()
            senha = form['senha_1'].value()

            # Verifica se o nome de usuário já existe
            if User.objects.filter(username=nome).exists(): 
                return redirect('cadastro') # Redireciona para a página de cadastro
            
            # Cria o usuário
            usuario = User.objects.create_user( 
                username=nome, 
                email=email, 
                password=senha,
                first_name=primeiro,
                last_name=ultimo
            )
            usuario.save() # Salva o usuário no banco de dados
            return redirect('login') # Redireciona para a página de login



    return render(request, 'usuarios/cadastro.html', {'form': form})
