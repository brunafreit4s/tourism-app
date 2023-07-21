from rest_framework.serializers import ModelSerializer
from comentarios.api.viewsets import Comentarios

class ComentariosSerializer(ModelSerializer):
    class Meta:
        model = Comentarios
        fields = ['usuario', 'comentario', 'data']