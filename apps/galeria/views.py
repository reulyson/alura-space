from django.shortcuts import render
from .models import Fotografia
from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

''' Função para renderizar a página inicial da galeria '''

@login_required
def index(request):
    
    # Verifica se o usuário está logado
    if not request.user.is_authenticated:
        messages.error(request, 'Você precisa estar logado para acessar essa página.')
        return redirect('login')
    dados = Fotografia.objects.order_by('-data_fotografia').filter(publicada=True) # Ordena as fotografias por data de publicação e exibe apenas as fotografias publicadas

    # Adicionando as categorias
    categorias = Fotografia.OPCOES_CATEGORIA 
    return render(request,'galeria/index.html', {
        'cards': dados,
        'categorias': categorias,
        'usa_bootstrap': False
    }) # Renderiza a página inicial da galeria

''' Função para renderizar a página da fotografia '''
def imagem(request, foto_id):

    # Verifica se o usuário está logado
    if not request.user.is_authenticated:
        messages.error(request, 'Você precisa estar logado para acessar essa página.')
        return redirect('login')

    fotografia = get_object_or_404(Fotografia, pk=foto_id) # Busca a fotografia pelo id
    
    # Adicionando as categorias
    categorias = Fotografia.OPCOES_CATEGORIA 
    return render(request, 'galeria/imagem.html', {
        'fotografia': fotografia,
        'categorias': categorias,
        'usa_bootstrap': False
    }) # Renderiza a página da fotografia

def deletar_foto(request, foto_id):

    
    foto = get_object_or_404(Fotografia, id=foto_id) # Busca a fotografia pelo id
    
    # Verifica se o usuário logado tem permissão para excluir a fotografia
    if request.user == foto.usuario:
        foto.delete() # Exclui a fotografia
        messages.success(request, "Foto excluída com sucesso!")
        return redirect('index')  # Redireciona para a página principal
    else:
        messages.error(request, "Você não tem permissão para excluir esta foto.")
        return redirect('imagem', foto_id=foto_id)  # Volta para a página da foto
        

def buscar(request):

    # Verifica se o usuário está logado
    if not request.user.is_authenticated:
        messages.error(request, 'Você precisa estar logado para acessar essa página.')
        return redirect('login')

    busca = Fotografia.objects.order_by('-data_fotografia').filter(publicada=True) 

    # Verifica se o usuário digitou algo no campo de busca
    if 'buscar' in request.GET:
        nome_a_buscar = request.GET['buscar'] # Armazena o que o usuário digitou no campo de busca
        if nome_a_buscar:
            busca = busca.filter(nome__icontains=nome_a_buscar) # Faz a busca pelo nome da fotografia

    # Adicionando as categorias
    categorias = Fotografia.OPCOES_CATEGORIA        
    return render(request, 'galeria/buscar.html', {
        'cards': busca,
        'categorias': categorias
    })

def categoria(request, categoria_nome):

    # Verifica se o usuário está logado
    if not request.user.is_authenticated:
        messages.error(request, 'Você precisa estar logado para acessar essa página.')
        return redirect('login')

    # Mapeando as categorias
    MAPA_CATEGORIAS = {
        'NEBULOSA': 'NEBULOSA',
        'ESTRELAS': 'ESTRELAS',
        'PLANETA': 'PLANETA',
        'GALAXIA': 'GALAXIA'
    }

    # Obtém o valor correto para filtar as fotografias
    categoria_db = MAPA_CATEGORIAS.get(categoria_nome, categoria_nome)

    fotos = Fotografia.objects.filter(
        categoria=categoria_db,
        publicada=True
    ).order_by('-data_fotografia')

    # Adicionando as categorias
    categorias = Fotografia.OPCOES_CATEGORIA
    return render(request, 'galeria/categoria.html', {
        'fotos_categoria': fotos,
        'categorias': categorias
    })