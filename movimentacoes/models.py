from django.db import models
from materiais.models import Material
from usuarios.models import Usuario

class Movimentacao(models.Model):
    TIPOS = [
        ('E', 'Entrada'),
        ('S', 'Saída'),
    ]

    material = models.ForeignKey(Material, on_delete=models.PROTECT, related_name='movimentacoes')
    usuario = models.ForeignKey(Usuario, on_delete=models.PROTECT, related_name='movimentacoes')
    tipo = models.CharField(max_length=1, choices=TIPOS)
    quantidade = models.IntegerField()
    data_movimentacao = models.DateTimeField(auto_now_add=True)
    observacao = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.get_tipo_display()} - {self.material.nome} ({self.quantidade})"