from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

''' Estrutura do banco de dados da galeria '''
class Fotografia(models.Model):

    # definindo as categorias
    OPCOES_CATEGORIA = [
        ('NEBULOSA', 'Nebulosa'),
        ('ESTRELAS', 'Estrelas'),
        ('PLANETA', 'Planeta'),
        ('GALAXIA', 'Galaxia'),
    ]

    # definindo os campos
    nome = models.CharField(max_length=100, null=False, blank=False)
    legenda = models.CharField(max_length=150, null=False, blank=False)
    categoria = models.CharField(max_length=100, choices=OPCOES_CATEGORIA, default='')
    descricao = models.TextField(null=False, blank=False)
    foto = models.ImageField(upload_to='fotos/%Y/%m/%d', blank=True)
    publicada = models.BooleanField(default=True)
    data_fotografia = models.DateTimeField(default=datetime.now, blank=False)
    usuario = models.ForeignKey( # chave estrangeira
        to=User, # qual model esta sendo relacionada
        on_delete=models.SET_NULL, # o que fazer se o usuário for excluído
        null=True,
        blank=False,
        related_name='user' # nome da relação
    )

    ''' Retorna o nome da fotografia '''
    def __str__(self):
        return self.nome