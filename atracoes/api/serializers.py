from rest_framework.serializers import ModelSerializer
from atracoes.api.viewsets import Atracao

class AtracaoSerializer(ModelSerializer):
    class Meta:
        model = Atracao
        fields = ['nome', 'descricao', 'horario_func', 'idade_min', 'foto']