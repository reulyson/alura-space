from django.shortcuts import render, redirect # Importa as funções render e redirect
from django.contrib.auth.models import User # Importa o modelo User para usuários
from django.contrib import auth, messages # Importa o módulo auth para autenticação
from .forms import LoginForm, CadastroForm # Importa os formulários

def login(request): # Função para renderizar a página de login

    # Verifica se o usuário está logado
    if request.user.is_authenticated:
        messages.error(request, 'Você já está logado!')
        return redirect('index')

    form = LoginForm()

    if request.method == 'POST': 
        form = LoginForm(request.POST) 

        if form.is_valid(): 
            nome = form['nome_login'].value()
            senha = form['senha'].value()

            # Autentica o usuário
            usuario = auth.authenticate(request, 
                                        username=nome, 
                                        password=senha
                                    )
            if usuario is not None: # Verifica se o usuário foi autenticado
                auth.login(request, usuario) # Autentica o usuário
                messages.success(request, 'Login efetuado com sucesso!')
                return redirect('index') # Redireciona para a página inicial
            else:
                messages.error(request, 'Usuário ou senha inválidos!')
                return redirect('login') # Redireciona para a página de login
            
    return render(request, 'usuarios/login.html', {'form': form, 'usa_bootstrap': True})

def cadastro(request): # Função para renderizar a página de cadastro

    # Verifica se o usuário está logado
    if request.user.is_authenticated:
        messages.error(request, 'Você já está logado!')
        return redirect('index')

    form = CadastroForm()

    # Verifica se a requisição é do tipo POST (POST é usado para enviar dados)
    if request.method == 'POST': 
        form = CadastroForm(request.POST) # Cria um formulário com os dados da requisição

        if form.is_valid(): # Verifica se o formulário é válido
            
            # Armazena os dados do formulário
            primeiro = form['primeiro_nome'].value()
            ultimo = form['ultimo_nome'].value()
            nome = form['nome_cadastro'].value()
            email = form['email'].value()
            senha = form['senha_1'].value()

            # Verifica se o nome de usuário já existe
            if User.objects.filter(username=nome).exists():
                messages.error(request, 'Nome de usuário já existe!')
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
            messages.success(request, 'Cadastro efetuado com sucesso!')
            return redirect('login') # Redireciona para a página de login



    return render(request, 'usuarios/cadastro.html', {'form': form, 'usa_bootstrap': True})

def logout(request): # Função para deslogar o usuário
    auth.logout(request) # Desloga o usuário
    messages.success(request, 'Logout efetuado com sucesso!')
    return redirect('login')