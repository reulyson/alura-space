from django import forms
from  .models import Fotografia

class NovaImagemForm(forms.ModelForm):
    
    class Meta:
        model = Fotografia  # Especifique o modelo associado
        exclude = ['publicada','usuario',]
        labels = {
            'descricao': 'Descrição',
            'data_fotografia': 'Data da Fotografia',
        }

        widgets = {
            'nome': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ex: Nome da Estrela'
                }
            ),
            'legenda': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ex: nasa.org/NASA-Image-of-the-Day'
                }
            ),
            'categoria': forms.Select(attrs={'class': 'form-control'}),
            'descricao': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ex: Estrela no espaco'
                }
            ),
            'foto': forms.FileInput(attrs={'class': 'form-control', 'accept': 'image/*'}),
            'data_fotografia': forms.DateInput(
                format='%Y-%m-%d',
                attrs={
                    'type': 'date',
                    'class': 'form-control'
                    }
                ),
        }