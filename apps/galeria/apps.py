from django.apps import AppConfig

''' Classe para configuração da galeria '''
class GaleriaConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField' # Padrão
    name = 'galeria' # Nome da aplicação
