from gestionProductos.models import G1_PRODUCTO
from gestionProductos.models import GZZ_PRODUCTO_CATEGORIA
from rest_framework import serializers


class ProductoCategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = GZZ_PRODUCTO_CATEGORIA
        fields = '__all__'



class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = G1_PRODUCTO
        fields = '__all__'