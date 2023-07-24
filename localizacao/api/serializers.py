from rest_framework.serializers import ModelSerializer
from localizacao.models import Localizacao

class LocalizacaoSerializer(ModelSerializer):
    class Meta:
        model = Localizacao
        fields = ['linha_1', 'linha_2', 'cidade', 'estado', 'pais']