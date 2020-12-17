from gestionPedidos.models import G4_COMANDA
from gestionPedidos.models import GZZ_ESTADO_PEDIDO
from gestionPedidos.models import G4Z_COMANDA_PRODUCTO
from rest_framework import serializers


class ComandaSerializer(serializers.ModelSerializer):
    class Meta:
        model = G4_COMANDA
        fields = '__all__'



class EstadoPedidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = GZZ_ESTADO_PEDIDO
        fields = '__all__'


class ComandaProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = G4Z_COMANDA_PRODUCTO
        fields = '__all__'