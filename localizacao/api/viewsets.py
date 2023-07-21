from rest_framework.viewsets import ModelViewSet
from localizacao.models import Localizacao
from .serializers import LocalizacaoSerializer

class LocalizacaoViewSet(ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    queryset = Localizacao.objects.all()
    serializer_class = LocalizacaoSerializer