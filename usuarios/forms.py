from typing import Any
from django import forms
from django.contrib.auth.models import User # Importa o modelo User para usuários
from  galeria.models import Fotografia


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

    def clean_nome_cadastro(self): # Funcao para verificar se o nome de usuário possui espaços
        nome = self.cleaned_data['nome_cadastro'] 

        if nome:
            nome = nome.strip() # Remove espaços em branco no inicio e fim
            if ' ' in nome: # Verifica se o nome possui espaços
                raise forms.ValidationError('Não é possivel inserir espaços nesse campo.')
            else:
                return nome
        
    def clean_senha_2(self): # Funcao para verificar se as senhas sao iguais
        senha_1 = self.cleaned_data['senha_1']
        senha_2 = self.cleaned_data['senha_2']           
        # Verifica se o formulário é válido
        
        if senha_1 and senha_2: # Verifica se as senhas são iguais
            if senha_1 != senha_2:
                raise forms.ValidationError('As senhas devem ser iguais.')
            else:
                return senha_2
            
class NovaImagemForm(forms.ModelForm):

    # Campos
    nome = forms.CharField(
        label='Nome', # Rotulo
        required=True, # Obrigatorio
        max_length=100, # Tamanho
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Ex: Nome da Estrela'
            }
        ) 
    )

    legenda = forms.CharField(
        label='Legenda', # Rotulo
        required=True, # Obrigatorio
        max_length=150, # Tamanho
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Ex: nasa.org/NASA-Image-of-the-Day'
            }
        ) 
    )

    categoria = forms.ChoiceField(
        label='Categoria', # Rotulo
        required=True, # Obrigatorio
        choices=Fotografia.OPCOES_CATEGORIA,
        widget=forms.Select(
            attrs={
                'class': 'form-control'
            }
        ) 
    )

    descricao = forms.CharField(
        label='Descricao', # Rotulo
        required=True, # Obrigatorio
        max_length=100, # Tamanho
        widget=forms.Textarea(
            attrs={
                'class': 'form-control',
                'placeholder': 'Ex: Estrela no espaco'
            }
        )
    )

    foto = forms.ImageField(
        label='Foto', # Rotulo
        required=True, # Obrigatorio
        widget=forms.FileInput(
            attrs={
                'class': 'form-control',
                'accept': 'image/*'
            }
        )
    )

    publicada = forms.BooleanField(
        label='Publicar', # Rotulo
        required=False, # Obrigatorio
        widget=forms.CheckboxInput(
            attrs={
                'class': 'form-check-input'
            }
        )
    )

    def clean_foto(self):
        foto = self.cleaned_data.get('foto')
        if not foto:
            raise forms.ValidationError("Você deve selecionar uma imagem.")
        return foto

    class Meta:
        model = Fotografia  # Especifique o modelo associado
        fields = ['nome', 'legenda', 'categoria', 'descricao', 'foto', 'publicada']
    