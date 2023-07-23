from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.decorators import action
from core.models import PontoTuristico
from .serializers import PontoTuristicoSerializer

class PontoTuristicoViewSet(ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    # queryset = PontoTuristico.objects.filter(aprovado=True)
    serializer_class = PontoTuristicoSerializer


    """ 
        Na ModelViewSet já existem métodos padrões,
        mas é possível sobrescrever conforme abaixo:
    """
    def get_queryset(self):
        return PontoTuristico.objects.filter(aprovado=True)
    
    def list(self, request, *args, **kwargs):
        return Response({'teste', 123456})
    
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
    
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)
    
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)
    
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)
    
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)
    
    # Cria um novo método utilizando action
    @action(methods=['get'], detail=True)
    def denunciar(self, request, pk=None):
        pass