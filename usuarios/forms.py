from django import forms

''' Formulario de login '''
class LoginForm(forms.Form):

    # Campos
    nome_login = forms.CharField(
        label='Nome de Login', # Rotulo
        required=True, # Obrigatorio
        max_length=100, # Tamanho
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Ex: João Silva'
            }
        ) 
    )

    senha = forms.CharField(
        label='Senha', 
        required=True,
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Digite sua senha'
            }
        ) # Campo de senha
    )

class CadastroForm(forms.Form):

    # Campos
    primeiro_nome = forms.CharField(
        label='Nome', # Rotulo
        required=True, # Obrigatorio
        max_length=100, # Tamanho
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Ex: João'
            }
        )
    
    )

    ultimo_nome = forms.CharField(
        label='Sobrenome', # Rotulo
        required=True, # Obrigatorio
        max_length=100, # Tamanho
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Ex: Silva'
            }
        )
    )
    nome_cadastro = forms.CharField(
        label='Usuário', # Rotulo
        required=True, # Obrigatorio
        max_length=100, # Tamanho
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Ex: joao'
            }
        ) 
    )

    email = forms.EmailField(
        label='Email', 
        required=True,
        max_length=100,
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Ex: joaosilva@xpto.com'
            }
        ) # Campo de senha
    )

    senha_1 = forms.CharField(
        label='Senha', 
        required=True,
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Digite sua senha'
            }
        ) # Campo de senha
    )

    senha_2 = forms.CharField(
        label='Confirmação de senha', 
        required=True,  
        max_length=70,  
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Digite sua senha novamente'
            }
        )
    )