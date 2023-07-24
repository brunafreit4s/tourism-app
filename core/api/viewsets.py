from rest_framework.viewsets import ModelViewSet
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from core.models import PontoTuristico
from .serializers import PontoTuristicoSerializer

class PontoTuristicoViewSet(ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    # queryset = PontoTuristico.objects.filter(aprovado=True)
    serializer_class = PontoTuristicoSerializer

    # Autenticação
    #authentication_classes = (TokenAuthentication,)
    #permission_classes = (IsAuthenticated,)
    
    """ 
        permission_classes:
            Permite apenas a leitura (GET) da api,
            Não permitindo os demais verbos
    """
    # permission_classes = (IsAuthenticatedOrReadOnly,)

    """ 
        Na ModelViewSet já existem métodos padrões,
        mas é possível sobrescrever conforme abaixo:
    """
    def get_queryset(self):
        id = self.request.query_params.get('id', None)
        nome = self.request.query_params.get('nome', None)
        descricao = self.request.query_params.get('descricao', None)
        queryset = PontoTuristico.objects.all()

        if id:
            queryset = PontoTuristico.objects.filter(pk=id)

        # __iexact = Case insensitive - Ignora diferenciação de maiúsculas ou minúsculas
        if nome:
            queryset = queryset.filter(nome__iexact=nome)

        if descricao:
            queryset = queryset.filter(descricao__iexact=descricao)

        return queryset
        #return PontoTuristico.objects.filter(aprovado=True)
    
    def list(self, request):
        return super(PontoTuristicoViewSet, self).list(request)
    
    def create(self, request, *args, **kwargs):
        return super(PontoTuristicoViewSet, self).create(request, *args, **kwargs)
    
    def destroy(self, request, *args, **kwargs):
        return super(PontoTuristicoViewSet, self).destroy(request, *args, **kwargs)
    
    def retrieve(self, request, *args, **kwargs):
        return super(PontoTuristicoViewSet, self).retrieve(request, *args, **kwargs)
    
    def update(self, request, *args, **kwargs):
        return super(PontoTuristicoViewSet, self).update(request, *args, **kwargs)
    
    def partial_update(self, request, *args, **kwargs):
        return super(PontoTuristicoViewSet, self).partial_update(request, *args, **kwargs)
    
    # Cria um novo método utilizando action
    @action(methods=['get'], detail=True)
    def denunciar(self, request, pk=None):
        return super(PontoTuristicoViewSet, self).list(request)