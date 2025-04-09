from django.shortcuts import render
from .models import Fotografia
from django.shortcuts import get_object_or_404

''' Função para renderizar a página inicial da galeria '''
def index(request):

    dados = Fotografia.objects.order_by('-data_fotografia').filter(publicada=True) # Ordena as fotografias por data de publicação e exibe apenas as fotografias publicadas
    return render(request,'galeria/index.html', {'cards': dados}) # Renderiza a página inicial da galeria

''' Função para renderizar a página da fotografia '''
def imagem(request, foto_id):

    fotografia = get_object_or_404(Fotografia, pk=foto_id) # Busca a fotografia pelo id
    return render(request, 'galeria/imagem.html', {'fotografia': fotografia}) # Renderiza a página da fotografia

def buscar(request):

    busca = Fotografia.objects.order_by('-data_fotografia').filter(publicada=True) 

    # Verifica se o usuário digitou algo no campo de busca
    if 'buscar' in request.GET:
        nome_a_buscar = request.GET['buscar'] # Armazena o que o usuário digitou no campo de busca
        if nome_a_buscar:
            busca = busca.filter(nome__icontains=nome_a_buscar) # Faz a busca pelo nome da fotografia
    return render(request, 'galeria/buscar.html', {'cards': busca})