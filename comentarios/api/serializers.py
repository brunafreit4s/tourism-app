from rest_framework.serializers import ModelSerializer
from comentarios.models import Comentarios

class ComentariosSerializer(ModelSerializer):
    class Meta:
        model = Comentarios
        fields = ['usuario', 'comentario', 'data']