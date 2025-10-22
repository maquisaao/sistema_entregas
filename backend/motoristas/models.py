from django.db import models

class Motorista(models.Model):
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=14, unique=True)
    telefone = models.CharField(max_length=20)
    ativo = models.BooleanField(default=True)
    contagem_corridas_dia = models.IntegerField(default=0)
    placa_moto = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.nome} - {self.placa_moto}"
