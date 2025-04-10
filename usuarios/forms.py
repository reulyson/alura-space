from django import forms

''' Formulario de login '''
class LoginForm(forms.Form):

    # Campos
    nome_login = forms.CharField(
        label='Nome de Login', # Rotulo
        required=True, # Obrigatorio
        max_length=100 # Tamanho
    )

    senha = forms.CharField(
        label='Senha', 
        required=True,
        max_length=70,
        widget=forms.PasswordInput # Campo de senha
    )
