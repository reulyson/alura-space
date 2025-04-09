from django.urls import path
from .views import login, cadastro

''' Caminhos para as páginas da galeria '''
urlpatterns = [
    path('login/', login, name='login'),
    path('cadastro/', cadastro, name='cadastro'),
]