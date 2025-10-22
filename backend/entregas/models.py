from django.db import models

class Motorista(models.Model):
    nome = models.CharField(max_length=100)
    telefone = models.CharField(max_length=20)
    email = models.EmailField()
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return self.nome

class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    endereco = models.CharField(max_length=200)
    telefone = models.CharField(max_length=20)

    def __str__(self):
        return self.nome

class Entrega(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    motorista = models.ForeignKey(Motorista, on_delete=models.SET_NULL, null=True, blank=True)
    endereco_entrega = models.CharField(max_length=200)
    data_prevista = models.DateTimeField()
    entregue = models.BooleanField(default=False)
    valor = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Entrega para {self.cliente.nome} em {self.data_prevista}"
