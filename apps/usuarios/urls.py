from django.urls import path
from .views import login, cadastro, logout

''' Caminhos para as páginas da galeria '''
urlpatterns = [
    path('', login, name='login'),
    path('login', login, name='login'),
    path('cadastro', cadastro, name='cadastro'),
    path('logout', logout, name='logout'),
]