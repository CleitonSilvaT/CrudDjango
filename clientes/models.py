from django.db import models

class Cliente(models.Model):
    nome = models.CharField(max_length=50)
    email = models.EmailField()
    cpf = models.CharField(max_length=11, unique=True) # Tamanho contando os pontos
    data_criacao = models.DateField(auto_now_add=True)

    def __str__(self): # Definir o que será mostrado no Admin
        return self.name
    