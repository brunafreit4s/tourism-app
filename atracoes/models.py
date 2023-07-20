from django.db import models

class Atracao(models.Model):
    nome = models.CharField(max_length=150)
    descricao = models.TextField(max_length=500)
    horario_func = models.TextField()
    idade_min = models.IntegerField()

    def __str__(self) -> str:
        return self.nome