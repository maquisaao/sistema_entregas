from django.contrib import admin
from .models import Motorista

@admin.register(Motorista)
class MotoristaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cpf', 'telefone', 'ativo', 'contagem_corridas_dia', 'placa_moto')
