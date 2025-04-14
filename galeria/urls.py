from django.urls import path
from .views import index, imagem, buscar, categoria, deletar_foto

''' Caminhos para as páginas da galeria '''
urlpatterns = [
    path('', index, name='index'), # Página principal
    path('imagem/<int:foto_id>', imagem, name='imagem'), # Página da fotografia
    path('buscar/', buscar, name='buscar'), # Página de busca
    path('categoria/<str:categoria_nome>', categoria, name='categoria'), # Página da categoria
    path('deletar/<int:foto_id>', deletar_foto, name='deletar'), # Página de exclusão
]