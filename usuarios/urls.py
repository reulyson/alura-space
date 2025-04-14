from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import login, cadastro, logout, novas_fotos

''' Caminhos para as páginas da galeria '''
urlpatterns = [
    path('login', login, name='login'),
    path('cadastro', cadastro, name='cadastro'),
    path('logout', logout, name='logout'),
    path('novas_fotos', novas_fotos, name='novas_fotos'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)