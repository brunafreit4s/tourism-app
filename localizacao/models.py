from django.db import models

class Localizacao(models.Model):
    linha_1 = models.CharField(max_length=150)
    linha_2 = models.CharField(max_length=150, null=True, blank=True)
    cidade = models.CharField(max_length=100)
    estado = models.CharField(max_length=50)
    pais = models.CharField(max_length=70)
    latitude = models.IntegerField(null=True, blank=True)
    longitude = models.IntegerField(null=True, blank=True)

    def __str__(self) -> str:
        return self.linha_1