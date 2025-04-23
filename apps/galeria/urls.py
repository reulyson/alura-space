from django.urls import path
from .views import index, imagem, buscar, categoria, novas_fotos, deletar_foto, editar_foto, teste
from django.conf.urls.static import static
from django.conf import settings

''' Caminhos para as páginas da galeria '''
urlpatterns = [
    path('home', index, name='index'), # Página principal
    path('imagem/<int:foto_id>', imagem, name='imagem'), # Página da fotografia
    path('buscar/', buscar, name='buscar'), # Página de busca
    path('categoria/<str:categoria_nome>', categoria, name='categoria'), # Página da categoria
    path('novas-fotos', novas_fotos, name='novas_fotos'), # Página de nova fotografia
    path('editar-foto/<int:foto_id>', editar_foto, name='editar_foto'), # Página de edição
    path('deletar/<int:foto_id>', deletar_foto, name='deletar'), # Rota para deletar
    path('teste', teste, name='teste'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)