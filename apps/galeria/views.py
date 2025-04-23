from django.shortcuts import render
from .models import Fotografia
from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import NovaImagemForm # Importa os formulários

''' Função para renderizar a página inicial da galeria '''
@login_required
def index(request):
    
    # Verifica se o usuário está logado
    if not request.user.is_authenticated:
        messages.error(request, 'Você precisa estar logado para acessar essa página.')
        return redirect('login')
    
    dados = Fotografia.objects.order_by('-data_fotografia').filter(publicada=True) # Ordena as fotografias por data de publicação e exibe apenas as fotografias publicadas
    return render(request,'galeria/index.html', {'cards': dados}) # Renderiza a página inicial da galeria

''' Função para renderizar a página da fotografia '''
def imagem(request, foto_id):

    # Verifica se o usuário está logado
    if not request.user.is_authenticated:
        messages.error(request, 'Você precisa estar logado para acessar essa página.')
        return redirect('login')

    fotografia = get_object_or_404(Fotografia, pk=foto_id) # Busca a fotografia pelo id
    return render(request, 'galeria/imagem.html', {
        'fotografia': fotografia,
        'usa_bootstrap': True,
    }) # Renderiza a página da fotografia

''' Função que realiza a busca de fotografias '''
def buscar(request):

    if not request.user.is_authenticated:  # Verifica se o usuário está logado
        messages.error(request, 'Você precisa estar logado para acessar essa página.')
        return redirect('login')

    busca = Fotografia.objects.order_by('-data_fotografia').filter(publicada=True) # Ordena as fotografias por data de publicação e exibe apenas as fotografias publicadas
    if 'buscar' in request.GET:  # Verifica se o usuário digitou algo no campo de busca
        nome_a_buscar = request.GET['buscar'] # Armazena o que o usuário digitou no campo de busca
        if nome_a_buscar:
            busca = busca.filter(nome__icontains=nome_a_buscar) # Faz a busca pelo nome da fotografia

    return render(request, 'galeria/index.html', {'cards': busca,})

''' Função que filtra as fotografias por categoria '''
def filtro(request, categoria):
     
     fotos = Fotografia.objects.order_by('-data_fotografia').filter(publicada=True, categoria=categoria)
     return render(request, 'galeria/index.html', {'cards': fotos,})

''' Função para renderizar a página de nova fotografia '''
def novas_fotos(request):

    # Verifica se o usuário está logado
    if not request.user.is_authenticated:
        messages.error(request, 'Você precisa estar logado para acessar essa página.')
        return redirect('login')

    form = NovaImagemForm() # Cria um formulário vazio
    if request.method == 'POST': # Verifica se a requisição é do tipo POST (POST é usado para enviar dados)
        form = NovaImagemForm(request.POST, request.FILES) # Cria um formulário com os dados da requisição
        if form.is_valid(): # Verifica se o formulário é válido
            try:
                fotografia = form.save(commit=False) # Valida os dados mas não sala no banco de dados
                fotografia.usuario = request.user # Armazena o usuário que fez a fotografia
                fotografia.save() # Salva a fotografia no banco de dados
                messages.success(request, 'Fotografia salva com sucesso!')
                return redirect('index') # Redireciona para a página inicial
            except Exception as e:
                messages.error(request, 'Erro ao salvar a fotografia!')

    return render(request, 'galeria/novas_fotos.html', {'form': form, 'usa_bootstrap': True})

''' Função para excluir uma fotografia '''
def deletar_foto(request, foto_id):

    fotografia= Fotografia.objects.get(id=foto_id) # Busca a fotografia pelo id
    fotografia.delete() # Exclui a fotografia
    messages.success(request, "Foto excluída com sucesso!")
    return redirect('index')  # Volta para a página da fotografia

''' Função para editar uma fotografia '''
def editar_foto(request, foto_id):

    fotografia= Fotografia.objects.get(id=foto_id) # Busca a fotografia pelo id
    form = NovaImagemForm(instance=fotografia) # Cria um formulário com os dados da fotografia

    if request.method == 'POST':
        form = NovaImagemForm(request.POST, request.FILES, instance=fotografia)
        if form.is_valid(): # Verifica se o formulário é válido
            form.save() # Salva a fotografia no banco de dados
            messages.success(request, 'Fotografia salva com sucesso!')
            return redirect('index')  # Redireciona para a página inicial
    
    return render(request, 'galeria/editar_foto.html', {
        'form': form,
        'fotografia': fotografia,
        'usa_bootstrap': True
    })