from rest_framework.serializers import ModelSerializer
from core.api.viewsets import PontoTuristico

class PontoTuristicoSerializer(ModelSerializer):
    class Meta:
        model = PontoTuristico
        fields = ['id', 'nome', 'descricao']