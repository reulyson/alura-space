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
            