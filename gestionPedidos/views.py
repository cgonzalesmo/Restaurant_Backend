from gestionPedidos.models import G4_COMANDA
from gestionPedidos.models import GZZ_ESTADO_PEDIDO
from gestionPedidos.models import G4Z_COMANDA_PRODUCTO

from django.shortcuts import render

from rest_framework import viewsets
from gestionPedidos.serializers import ComandaSerializer
from gestionPedidos.serializers import EstadoPedidoSerializer
from gestionPedidos.serializers import ComandaProductoSerializer


# Create your views here.


class ComandaViewset(viewsets.ModelViewSet):
    queryset = G4_COMANDA.objects.all()
    serializer_class =ComandaSerializer

class EstadoPedidoViewset(viewsets.ModelViewSet):
    queryset = GZZ_ESTADO_PEDIDO.objects.all()
    serializer_class = EstadoPedidoSerializer

class ComandaProductoViewset(viewsets.ModelViewSet):
    queryset = G4Z_COMANDA_PRODUCTO.objects.all()
    serializer_class = ComandaProductoSerializer