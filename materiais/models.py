from django.db import models

class Material(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField(blank=True, null=True)
    quantidade = models.IntegerField(default=0)
    estoque_minimo = models.IntegerField(default=5)
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome