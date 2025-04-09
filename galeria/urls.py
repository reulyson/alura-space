from django.urls import path, include
from .views import index, imagem, buscar

''' Caminhos para as páginas da galeria '''
urlpatterns = [
    path('', index, name='index'), # Página principal
    path('imagem/<int:foto_id>', imagem, name='imagem'), # Página da fotografia
    path('buscar/', buscar, name='buscar'), # Página de busca
]