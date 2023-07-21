from rest_framework.serializers import ModelSerializer
from avaliacoes.api.viewsets import Avaliacao

class AvaliacaoSerializer(ModelSerializer):
    class Meta:
        model = Avaliacao
        fields = ['user', 'comentario', 'nota', 'data']