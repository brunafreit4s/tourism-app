from rest_framework.serializers import ModelSerializer
from core.models import PontoTuristico
from atracoes.api.serializers import AtracaoSerializer
from avaliacoes.api.serializers import AvaliacaoSerializer
from comentarios.api.serializers import ComentariosSerializer
from localizacao.api.serializers import LocalizacaoSerializer

class PontoTuristicoSerializer(ModelSerializer):
    atracoes = AtracaoSerializer(many=True)
    avaliacoes = AvaliacaoSerializer(many=True)
    comentarios = ComentariosSerializer(many=True)
    localizacao = LocalizacaoSerializer()

    class Meta:        
        model = PontoTuristico
        fields = ['id', 'nome', 'descricao', 'foto', 
                  'atracoes', 'avaliacoes', 'comentarios', 'localizacao',]
        