from django import forms
from .models import Cliente

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nome', 'cpf', 'email']
        widgets = {
            'nome': forms.TextInput(attrs={'placeholder':'informe o nome do cliente'}),
            'cpf': forms.TextInput(attrs={'placeholder':'Informe o cpf do cliente'}),
            'email': forms.TextInput(attrs={'placeholder':'Informe o email do cliente'})
        }